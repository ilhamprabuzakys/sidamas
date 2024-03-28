from django_filters.rest_framework import DjangoFilterBackend
from openpyxl import Workbook
from openpyxl.styles import alignment
from rest_framework import status, viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from users.models import Profile, Satker

from django.db.models import Count, Q

import openpyxl
from openpyxl.styles import Alignment
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.table import Table, TableStyleInfo

import re
import os
import codecs
import shutil
import datetime
import pandas as pd
from django.conf import settings

from sidamas import pagination

from kegiatan import models
from kegiatan.api import serializers
from kegiatan.api import filters
from users.serializers import SatkerSerializer
from users.models import Satker

def get_kegiatan_satker_status(request):
    satker = request.user.profile.satker
    
    """
        Mapping :
        Satker Level       Status
        0 : BNNP        -> 2 : Pusat
        1 : BNNK        -> 1 : BNNP
        2 : Pusat       -> 2 : Pusat
    """

    status_map = {
        0: 1,
        1: 0,
        2: 2
    }
    
    status = status_map.get(satker.level, None)
    
    return status

def get_tanggal_kegiatan(self, tanggal_awal, tanggal_akhir=None):
    start = datetime.date.fromisoformat(f'{tanggal_awal}')
    start_date = start.strftime('%-d')
    start_month = start.strftime('%B')
    start_year = start.strftime('%Y')
    
    nama_bulan = {
        "January": "Januari",
        "February": "Februari",
        "March": "Maret",
        "April": "April",
        "May": "Mei",
        "June": "Juni",
        "July": "Juli",
        "August": "Agustus",
        "September": "September",
        "October": "Oktober",
        "November": "November",
        "December": "Desember"
    }

    if tanggal_akhir:
        end = datetime.date.fromisoformat(f'{tanggal_akhir}')
        end_date = end.strftime('%-d')
        end_month = end.strftime('%B')
        end_year = end.strftime('%Y')

        if start_month == end_month and start_year == end_year:
            return f"{start_date} - {end_date} {nama_bulan[start_month]} {start_year}"
        elif start_year != end_year:
            return f"{start.strftime('%-d')} {nama_bulan[start_month]} {start_year} - {end.strftime('%-d')} {nama_bulan[end_month]} {end_year}"
        else:
            return f"{start.strftime('%-d')} {nama_bulan[start_month]} - {end.strftime('%-d')} {nama_bulan[end_month]} {end_year}"
    else:
        return f"{start.strftime('%-d')} {nama_bulan[start_month]} {start_year}"

class DAYATIF_BINAAN_TEKNIS_ViewSet(viewsets.ModelViewSet):
    queryset = models.DAYATIF_BINAAN_TEKNIS.objects.all().order_by('-tanggal_awal')
    serializer_class = serializers.DAYATIF_BINAAN_TEKNIS_Serializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = pagination.Page10NumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.DAYATIF_BINAAN_TEKNIS_Filters
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, status=get_kegiatan_satker_status(self.request))

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
    
    @action(detail=False)
    def get_one_row_data(self, request):
        
        serialized_data = self.get_flat_values(request)

        return Response(serialized_data, status=status.HTTP_200_OK)

    def get_flat_values(self, request):
        satker = self.request.user.profile.satker
        satker_provinsi = satker.provinsi_id
        satker_level = satker.level

        data = models.DAYATIF_BINAAN_TEKNIS.objects.values(
            'id', 'satker_id', 'satker__nama_satker', 'tanggal_awal', 'tanggal_akhir',
            'jumlah_hari_pelaksanaan', 'satker_target', 'satker_target__nama_satker', 'jumlah_peserta', 'tujuan', 'kendala', 'kesimpulan', 'tindak_lanjut', 'dokumentasi', 'status'
        ).order_by(
            'satker__nama_satker'
        )

        if satker_level == 1:
            data = data.filter(satker_id=satker, satker__level=satker_level)
        elif satker_level == 0:
            data = data.filter(satker__provinsi_id=satker_provinsi, satker__level=satker_level, status__gt=0)
        elif satker_level == 2:
            data = data.filter(status=2)
    
        serialized_data = []
        for item in data:
            serialized_item = {
                'id': item['id'],
                'satker_id': item['satker_id'],
                'nama_satker': item['satker__nama_satker'],
                'tanggal_awal': item['tanggal_awal'],
                'tanggal_akhir': item['tanggal_akhir'],
                'jumlah_hari_pelaksanaan': item['jumlah_hari_pelaksanaan'],
                'satker_target': item['satker_target'],
                'nama_satker_target': item['satker_target__nama_satker'],
                'jumlah_peserta': item['jumlah_peserta'],
                'tujuan': item['tujuan'],
                'kendala': item['kendala'],
                'kesimpulan': item['kesimpulan'],
                'tindak_lanjut': item['tindak_lanjut'],
                'dokumentasi': item['dokumentasi'],
                'status': item['status'],
                'satker_level': satker_level
            }
            serialized_data.append(serialized_item)
        
        return serialized_data
    
    @action(detail=False)
    def get_all_data(self, request):
        serialized_data = self.get_serialized_data(request)
        
        return Response(serialized_data, status=status.HTTP_200_OK)

    def get_serialized_data(self, request):
        search = request.GET.get("s", None)
        satker = self.request.user.profile.satker
        
        # print(f'User Profile Satker ID {satker.pk}')
        # print(f'User Profile Satker Level {satker.level}')
        # print(f'User Profile Satker Provinsi {satker.provinsi_id}')
        
        queryset = None
        
        # solo leveling
        if satker.level == 1:
            # BNNK
            queryset = models.DAYATIF_BINAAN_TEKNIS.objects.filter(
                satker_id=satker.pk
            ).values(
                'satker_id', 'satker__nama_satker', 'status'
            ).annotate(
                jumlah_kegiatan=Count('id')
            ).order_by(
                'satker_id'
            )
            
        elif satker.level == 0:
            # BNNP
            queryset = models.DAYATIF_BINAAN_TEKNIS.objects.filter(
                status__gt=0,
                satker__provinsi_id=satker.provinsi_id
            ).values(
                'satker_id', 'satker__nama_satker', 'status'
            ).annotate(
                jumlah_kegiatan=Count('id')
            ).order_by(
                'satker_id'
            )
        elif satker.level == 2:
            # BNNP Pusat
            queryset = models.DAYATIF_BINAAN_TEKNIS.objects.filter(
                status=2
            ).values(
                'satker_id', 'satker__nama_satker', 'status'
            ).annotate(
                jumlah_kegiatan=Count('id')
            ).order_by(
                'satker_id'
            )
        else:
            raise ValueError(f"Invalid satker level: {satker.level}")
        
        print('Hasil query :', len(queryset))
        
        if search: queryset = queryset.filter(Q(satker__nama_satker__icontains=search))
        
        serialized_data = []
        
        for index, item in enumerate(queryset):
            serialized_item = {
                'no': index + 1,
                'status': item['status'],
                'satker_id': item['satker_id'],
                'nama_satker': item['satker__nama_satker'],
                'jumlah_kegiatan': item['jumlah_kegiatan'],
                'daftar_kegiatan': self.get_detail_data(item['satker_id'])
            }
            serialized_data.append(serialized_item)

        return serialized_data


    def get_detail_data(self, satker_id):
        data = models.DAYATIF_BINAAN_TEKNIS.objects.filter(satker_id=satker_id).values(
            'id', 'status', 'satker_id', 'satker_target__id', 'satker_target__nama_satker', 'tanggal_awal', 'tanggal_akhir',
            'jumlah_hari_pelaksanaan', 'jumlah_peserta', 'tujuan', 'kendala', 'kesimpulan',
            'tindak_lanjut', 'dokumentasi'
        ).order_by('-tanggal_awal')
    
        serialized_data = []
        for item in data:
            serialized_item = {
                'id': item['id'],
                'status': item['status'],
                'satker_parent_id': item['satker_id'],
                'satker_id': item['satker_target__id'],
                'nama_satker': item['satker_target__nama_satker'],
                'tanggal_awal': item['tanggal_awal'],
                'tanggal_akhir': item['tanggal_akhir'],
                'jumlah_hari_pelaksanaan': item['jumlah_hari_pelaksanaan'],
                'jumlah_peserta': item['jumlah_peserta'],
                'tujuan': item['tujuan'],
                'kendala': item['kendala'],
                'kesimpulan': item['kesimpulan'],
                'tindak_lanjut': item['tindak_lanjut'],
                'dokumentasi': item['dokumentasi'],
            }
            serialized_data.append(serialized_item)

        return serialized_data
    
    @action(detail=True, methods=['delete'])
    def delete_all_kegiatan(self, request, pk=None):
        try:
            deleted_count, _ = models.DAYATIF_BINAAN_TEKNIS.objects.filter(satker_id=pk).delete()
            
            return Response({
                'status': deleted_count > 0,
                'deleted_count' : deleted_count,
                'message': 'Data kegiatan berhasil dihapus' if deleted_count > 0 else f'Data kegiatan dari Satker ID {pk} tidak ditemukan',
                'satker_id': pk,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'status': False,
                'message': f'Gagal saat menghapus semua kegiatan pada satker_id {pk}',
                'satker_id': pk,
                'error': f'{str(e)}'
            }, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post'])
    def semua_kegiatan(self, request):
        tipe = request.data.get("tipe", 'kirim')
        satker_id = request.data.get("satker_id", None)
        nama_satker = request.data.get("nama_satker", None)
        
        try:
            satker_instance = Satker.objects.filter(nama_satker=nama_satker).first() if not satker_id else Satker.objects.filter(pk=satker_id).first()
            satker_parent = {}
            
            if satker_instance.level == 1:
                satker_parent_instance = satker_instance.parent
                satker_parent['id'] = satker_parent_instance.pk
                satker_parent['keterangan'] = satker_parent_instance.nama_satker
            elif satker_instance.level == 0:
                satker_parent['id'] = 213
                satker_parent['keterangan'] = 'BNN Pusat'
            else:
                satker_parent['id'] = 0
                satker_parent['keterangan'] = ''
                
            kegiatan = models.DAYATIF_BINAAN_TEKNIS.objects.filter(satker_id=satker_instance.pk)
            message = ''
            
            if tipe == 'kirim':
                if satker_instance.level == 0:
                    kegiatan.update(status=2)
                elif satker_instance.level == 1:
                    kegiatan.update(status=1)
                    
                message = f'Data kegiatan dari Satuan Kerja {satker_instance.nama_satker} berhasil dikirim ke {satker_parent.get("keterangan")}'
            else:
                if satker_instance.level == 0:
                    kegiatan.update(status=1)
                elif satker_instance.level == 1:
                    kegiatan.update(status=0)
                
                message = f'Data kegiatan dari Satuan Kerja {satker_instance.nama_satker} berhasil dibatalkan dikirim ke {satker_parent.get("keterangan")}'
                
            return Response({
                'status': True,
                'message': message,
                'parent': satker_parent,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'status': False,
                'message': f'Gagal melakukan proses kirim/batal dari Satuan Kerja {nama_satker or satker_id}',
                'satker': nama_satker or satker_id,
                'error': f'{str(e)}'
            }, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post'])
    def kirim_kegiatan(self, request):
        kegiatan_id = request.data.get("kegiatan_id", None)
        kegiatan_id = int(kegiatan_id) if kegiatan_id else kegiatan_id
        
        try:
            satker_instance = self.request.user.profile.satker
            satker_parent = {}
            
            if satker_instance.level == 1:
                satker_parent_instance = satker_instance.parent
                satker_parent['id'] = satker_parent_instance.pk
                satker_parent['keterangan'] = satker_parent_instance.nama_satker
            elif satker_instance.level == 0:
                satker_parent['id'] = 213
                satker_parent['keterangan'] = 'BNN Pusat'
            else:
                satker_parent['id'] = 0
                satker_parent['keterangan'] = ''
                
            kegiatan = models.DAYATIF_BINAAN_TEKNIS.objects.filter(pk=kegiatan_id).first()
            
            if satker_instance.level == 0: # BNNP ke Pusat
                kegiatan.status = 2
            elif satker_instance.level == 1: # BNNK ke BNNP
                kegiatan.status = 1
            
            kegiatan.save()
                
            return Response({
                'status': True,
                'message': f'Data kegiatan ID {kegiatan_id} dari Satuan Kerja {satker_instance.nama_satker} berhasil dikirim ke {satker_parent.get("keterangan")}',
                'parent': satker_parent,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'status': False,
                'message': f'Gagal mengirim kegiatan ID {kegiatan_id} dari Satuan Kerja ID {satker_instance.pk}',
                'kegiatan_id': kegiatan_id,
                'error': f'{str(e)}'
            }, status=status.HTTP_400_BAD_REQUEST)
            
            
    @action(detail=False, methods=['post'])
    def export_data(self, request):
        satker = self.request.user.profile.satker
        
        tahun = datetime.datetime.now().year
        file_name = f'REKAPITULASI PEMBINAAN TEKNIS {satker.nama_satker.upper()} TAHUN {tahun}' if satker.level < 2 else f'REKAPITULASI PEMBINAAN TEKNIS BNNK & BNNP TAHUN {tahun}'
        base_path = 'media/kegiatan/binaan_teknis/exported'
        file_path = f'{base_path}/{file_name}.xlsx'
        
        shutil.rmtree(base_path)
        os.makedirs(base_path, exist_ok=True)
        
        base_url = self.request.build_absolute_uri('/')
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = f'Data Kegiatan Satuan Kerja {satker.nama_satker}'
        
        try:
            serialized_data = self.get_flat_values(request)

            # ======= HEADERS =======
            headers = [
                'NO.',
                'SATUAN KERJA PELAKSANA',
                'JUMLAH KEGIATAN',
                'STATUS',
                'NO.',
                'SATUAN KERJA TARGET',
                'TANGGAL',
                'JUMLAH HARI PELAKSANAAN',
                'JUMLAH PESERTA',
                'TUJUAN',
                'HAMBATAN/KENDALA',
                'KESIMPULAN',
                'TINDAK LANJUT',
                'DOKUMENTASI'
            ]
            
            # TUJUAN [J] SAMPAI KESIMPULAN [L] Ada Parent colspan 3 nya

            current_row = 4
            
            # ======= GENERATE HEADERS =======
            for item, header in enumerate(headers[:len(headers)], start=1):
                cell = sheet.cell(row=current_row, column=item, value=header)
                cell.fill = openpyxl.styles.PatternFill(start_color='D9EAD3', end_color='D9EAD3', fill_type='solid')
                cell.font = openpyxl.styles.Font(bold=True)
                cell.alignment = openpyxl.styles.Alignment(horizontal='center')
            
            current_row += 1
            
            no = 0
            no_child = 0
            current_group = None

            # ======= MAPPING DATA =======
            for row in serialized_data:
                if row['nama_satker'] != current_group:
                    if current_group is not None:
                        end_merge_row = current_row - 1
                        sheet.merge_cells(f'A{start_merge_row}:A{end_merge_row}')
                        sheet.merge_cells(f'B{start_merge_row}:B{end_merge_row}')  # Gabungkan sel grup
                    current_group = row['nama_satker']
                    start_merge_row = current_row
                    no += 1
                
                no_child += 1
                
                formatted_data = {}
                
                # ======= STATUS =======
                status_mapping = {
                    0: 'Belum dikirim',
                    1: 'Dikirim ke BNNP',
                    2: 'Dikirim ke BNN Pusat'
                }
                
                formatted_data['status'] = status_mapping.get(row['status'], '-')
                
                formatted_data['jumlah_kegiatan'] = f"{len(serialized_data)} kali"
                formatted_data['tanggal'] = get_tanggal_kegiatan(row['tanggal_awal'], row['tanggal_akhir'])
                formatted_data['jumlah_hari_pelaksanaan'] = f"{row['jumlah_hari_pelaksanaan']} hari"
                formatted_data['jumlah_peserta'] = f"{row['jumlah_peserta']} orang"
                
                for col in range(1, 5):  # Menggabungkan kolom dari A hingga D
                    celcol = sheet.cell(row=current_row, column=col, value=current_group)
                    celcol.font = openpyxl.styles.Font(bold=True)
                    celcol.alignment = Alignment(horizontal='center', vertical='center')
                    
                cell_e = sheet.cell(row=current_row, column=5, value=current_group)
                cell_e.font = openpyxl.styles.Font(bold=True)
                cell_e.alignment = Alignment(horizontal='center', vertical='center')
                
                cell_g = sheet.cell(row=current_row, column=7, value=current_group)
                cell_g.alignment = Alignment(horizontal='center', vertical='center')
                
                cell_h = sheet.cell(row=current_row, column=8, value=current_group)
                cell_h.alignment = Alignment(horizontal='center', vertical='center')
                
                cell_i = sheet.cell(row=current_row, column=9, value=current_group)
                cell_i.alignment = Alignment(horizontal='center', vertical='center')
                
                cell_n = sheet.cell(row=current_row, column=14, value=current_group)
                cell_n.alignment = Alignment(horizontal='center', vertical='center')

                data_row = [
                    no,
                    row['nama_satker'],
                    formatted_data['jumlah_kegiatan'],
                    formatted_data['status'],
                    no_child,
                    row['nama_satker_target'],
                    formatted_data['tanggal'],
                    formatted_data['jumlah_peserta'],
                    formatted_data['jumlah_hari_pelaksanaan'],
                    row['tujuan'],
                    row['kendala'],
                    row['kesimpulan'],
                    row['tindak_lanjut'],
                    # row['dokumentasi'],
                    f'=HYPERLINK("{base_url + row["dokumentasi"]}","Dokumentasi")',
                ]

                for item, value in enumerate(data_row[:len(headers)], start=1):
                    cell = sheet.cell(row=current_row, column=item, value=value)
                    cell.border = openpyxl.styles.Border(
                        left=openpyxl.styles.Side(style='thin'),
                        right=openpyxl.styles.Side(style='thin'),
                        top=openpyxl.styles.Side(style='thin'),
                        bottom=openpyxl.styles.Side(style='thin')
                    )

                current_row += 1

            # ======= MERGE CELL UNTUK GRUP TERAKHIR =======
            end_merge_row = current_row - 1
            sheet.merge_cells(f'A{start_merge_row}:A{end_merge_row}')
            sheet.merge_cells(f'B{start_merge_row}:B{end_merge_row}')
            sheet.merge_cells(f'C{start_merge_row}:C{end_merge_row}')
            sheet.merge_cells(f'D{start_merge_row}:D{end_merge_row}')

            # ======= AUTOFIT KOLOM =======
            for column in sheet.columns:
                max_length = 0
                for cell in column:
                    if cell.value:
                        max_length = max(max_length, len(str(cell.value)))
                adjusted_width = (max_length + 2) * 1.3
                sheet.column_dimensions[openpyxl.utils.get_column_letter(column[0].column)].width = adjusted_width
            
            sheet.column_dimensions['N'].width = 40

            # ======= SAVE FILE =======
            workbook.save(file_path)
            
            return Response({
                'status': True,
                'message': f'Data kegiatan dari {file_name} berhasil diekspor!',
                'file_path': f'/{file_path}'
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'status': False,
                'message': f'Gagal mengekspor daftar kegiatan dari Satuan Kerja {satker.nama_satker}',
                'error': f'{str(e)}'
            }, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post'])
    def export_data_old(self, request):
        satker = self.request.user.profile.satker
        tahun = datetime.datetime.now().year
        file_name = f'REKAPITULASI PEMBINAAN TEKNIS {satker.nama_satker.upper()} TAHUN {tahun}' if satker.level < 2 else f'REKAPITULASI PEMBINAAN TEKNIS BNNK & BNNP TAHUN {tahun}'
        base_path = 'media/kegiatan/binaan_teknis/exported'
        file_path = f'{base_path}/{file_name}.xlsx'
        
        try:
            serialized_data = self.get_serialized_data(request)
                
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            sheet.title = 'Data Kegiatan'
            
            # Menulis header untuk kolom A-D
            headers = ['No', 'Satuan Kerja Pelaksana', 'Jumlah Kegiatan', 'Status']
            for i, header in enumerate(headers, start=1):
                cell = sheet.cell(row=1, column=i, value=header)
                cell.fill = openpyxl.styles.PatternFill(start_color='D9EAD3', end_color='D9EAD3', fill_type='solid')
                cell.font = openpyxl.styles.Font(bold=True)  # Membuat teks tebal
                cell.alignment = openpyxl.styles.Alignment(horizontal='center')

            # Menulis header untuk kolom E seterusnya
            sub_headers = ['No', 'Satuan Kerja Target', 'Tanggal Awal', 'Tanggal Akhir', 'Jumlah Hari Pelaksanaan', 'Jumlah Peserta', 'Tujuan', 'Kendala', 'Kesimpulan', 'Tindak Lanjut', 'Dokumentasi']
            for i, sub_header in enumerate(sub_headers, start=len(headers)+1):
                cell = sheet.cell(row=1, column=i, value=sub_header)
                cell.fill = openpyxl.styles.PatternFill(start_color='D9EAD3', end_color='D9EAD3', fill_type='solid')
                cell.font = openpyxl.styles.Font(bold=True)  # Membuat teks tebal
                cell.alignment = openpyxl.styles.Alignment(horizontal='center')  # Mengatur alignment ke tengah

            # Menulis data ke file Excel
            current_row = 2
            for item in serialized_data:
                # Menulis data utama (main row)
                main_row = [item['no'], item['nama_satker'], item['jumlah_kegiatan'], item['status']]

                status_mapping = {
                    0: 'Belum dikirim',
                    1: 'Dikirim ke BNNP',
                    2: 'Dikirim ke BNN Pusat'
                }

                # Mengganti nilai status dengan label yang sesuai
                main_row[3] = status_mapping.get(item['status'], '-')

                # Menulis data utama ke file Excel
                for i, data in enumerate(main_row, start=1):
                    cell = sheet.cell(row=current_row, column=i, value=data)
                    cell.alignment = openpyxl.styles.Alignment(horizontal='center', vertical='center')

                # Menggabungkan sel untuk main row
                for col in range(1, 5):  # Menggabungkan kolom dari A hingga D
                    sheet.merge_cells(start_row=current_row, start_column=col, end_row=current_row+len(item['daftar_kegiatan'])+1, end_column=col)

                # Menulis data untuk sub row (nested row)
                nomor_kegiatan = 1
                for kegiatan in item['daftar_kegiatan']:
                    current_row += 1  # Increment current_row
                    
                    # Menambahkan nomor kegiatan
                    sheet.append(['', '', '', '', nomor_kegiatan, kegiatan['nama_satker'], kegiatan['tanggal_awal'], kegiatan['tanggal_akhir'], kegiatan['jumlah_hari_pelaksanaan'], kegiatan['jumlah_peserta'], kegiatan['tujuan'], kegiatan['kendala'], kegiatan['kesimpulan'], kegiatan['tindak_lanjut'], kegiatan['dokumentasi']])

                    # Mengatur alignment teks ke tengah untuk kolom F
                    for col in range(5, len(headers) + len(sub_headers)):
                        sheet.cell(row=current_row, column=col).alignment = openpyxl.styles.Alignment(horizontal='center', vertical='center')

                    nomor_kegiatan += 1  # Increment nomor kegiatan
                current_row += 1  # Increment current_row
                
            print(f'Current row : {current_row}')

            # Autofit kolom
            for column in sheet.columns:
                max_length = 0
                for cell in column:
                    if cell.value:
                        max_length = max(max_length, len(str(cell.value)))
                adjusted_width = (max_length + 2) * 1.2  # Meningkatkan lebar kolom untuk mengakomodasi teks yang lebih panjang
                sheet.column_dimensions[get_column_letter(column[0].column)].width = adjusted_width

            max_combined_cols = len(headers) + len(sub_headers)
            for row in sheet.iter_rows(min_row=1, max_row=current_row, min_col=1, max_col=max_combined_cols):
                for cell in row:
                    cell.border = openpyxl.styles.Border(left=openpyxl.styles.Side(style='thin'),
                                                        right=openpyxl.styles.Side(style='thin'),
                                                        top=openpyxl.styles.Side(style='thin'),
                                                        bottom=openpyxl.styles.Side(style='thin'))

            shutil.rmtree(base_path)
            os.makedirs(base_path, exist_ok=True)
            
            workbook.save(file_path)
            
            return Response({
                'status': True,
                'message': f'Data kegiatan dari {file_name} berhasil diexport',
                'file_path': f'/{file_path}',
                # 'data' : serialized_data,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'status': False,
                'message': f'Gagal mengexport kegiatan dari {file_name}',
                'error': f'{str(e)}'
            }, status=status.HTTP_400_BAD_REQUEST)
        
# ======= PEMETAAN POTENSI =======
class DAYATIF_PEMETAAN_POTENSI_LIST_ViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.DAYATIF_PEMETAAN_POTENSI.objects.all().filter(satker__parent__isnull=True).order_by('satker__satker_order', '-tanggal_awal', 'satker__order').distinct('satker__satker_order')
    serializer_class = serializers.DAYATIF_PEMETAAN_POTENSI_LIST_Serializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = pagination.Page10NumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.DAYATIF_PEMETAAN_POTENSI_Filters
    
    def get_queryset(self):
        satker = self.request.user.profile.satker
        satker_provinsi = satker.provinsi_id
        satker_level = satker.level

        queryset = super().get_queryset()
        
        if satker_level == 1:
            # BNNK
            queryset = queryset.filter(satker__id=satker)
        elif satker_level == 0:
            # BNNP
            queryset = queryset.filter(satker__provinsi_id=satker_provinsi, status__gt = 0)
        elif satker_level == 2:
            # PUSAT
            queryset = queryset.filter(status=2)
        return queryset

    @action(detail=False)
    def get_data_bnnk(self, request):
        satker = self.request.user.profile.satker

        data = models.DAYATIF_PEMETAAN_POTENSI.objects.all().filter(satker_id=satker).order_by('satker__nama_satker')
        
        serialized_data = [{
            'satker': SatkerSerializer(satker, many=False).data,
            'data': serializers.DAYATIF_PEMETAAN_POTENSI_Serializer(data, many=True).data
        }]
        
        return Response(serialized_data, status=status.HTTP_200_OK)
    
    def get_view_name(self):
        return "DAYATIF PEMETAAN POTENSI LIST"

class DAYATIF_PEMETAAN_POTENSI_ViewSet(viewsets.ModelViewSet):
    queryset = models.DAYATIF_PEMETAAN_POTENSI.objects.all().order_by('-tanggal_awal')
    serializer_class = serializers.DAYATIF_PEMETAAN_POTENSI_Serializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = pagination.Page10NumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.DAYATIF_PEMETAAN_POTENSI_Filters
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user, status=get_kegiatan_satker_status(self.request), satker=self.request.user.profile.satker)

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
        
    @action(detail=False)
    def get_all_data(self, request):
        serialized_data = self.get_serialized_data(request)
        
        return Response(serialized_data, status=status.HTTP_200_OK)

    def get_serialized_data(self, request):
        search = request.GET.get("s", None)
        satker = self.request.user.profile.satker
        
        # print(f'User Profile Satker ID {satker.pk}')
        # print(f'User Profile Satker Level {satker.level}')
        # print(f'User Profile Satker Provinsi {satker.provinsi_id}')
        
        queryset = None
        
        # solo leveling
        if satker.level == 1:
            # BNNK
            queryset = models.DAYATIF_PEMETAAN_POTENSI.objects.filter(
                satker_id=satker.pk
            ).values(
                'satker_id', 'satker__nama_satker', 'status'
            ).annotate(
                jumlah_kegiatan=Count('id')
            ).order_by(
                'satker_id'
            )
            
        elif satker.level == 0:
            # BNNP
            queryset = models.DAYATIF_PEMETAAN_POTENSI.objects.filter(
                status__gt=0,
                satker__provinsi_id=satker.provinsi_id
            ).values(
                'satker_id', 'satker__nama_satker', 'status'
            ).annotate(
                jumlah_kegiatan=Count('id')
            ).order_by(
                'satker_id'
            )
        elif satker.level == 2:
            # BNNP Pusat
            queryset = models.DAYATIF_PEMETAAN_POTENSI.objects.filter(
                status=2
            ).values(
                'satker_id', 'satker__nama_satker', 'status'
            ).annotate(
                jumlah_kegiatan=Count('id')
            ).order_by(
                'satker_id'
            )
        else:
            raise ValueError(f"Invalid satker level: {satker.level}")
        
        print('Hasil query :', len(queryset))
        
        if search: queryset = queryset.filter(Q(satker__nama_satker__icontains=search))
        
        serialized_data = []
        
        for index, item in enumerate(queryset):
            serialized_item = {
                'no': index + 1,
                'status': item['status'],
                'satker_id': item['satker_id'],
                'nama_satker': item['satker__nama_satker'],
                'jumlah_kegiatan': item['jumlah_kegiatan'],
                'daftar_kegiatan': self.get_detail_data(item['satker_id'])
            }
            serialized_data.append(serialized_item)

        return serialized_data

    def get_detail_data(self, satker_id):
        data = models.DAYATIF_PEMETAAN_POTENSI.objects.filter(satker_id=satker_id).values(
            'id', 'status', 'satker_id', 'satker__nama_satker', 'tanggal_awal', 'tanggal_akhir',
            'desa', 'nama_desa', 'kecamatan', 'nama_kecamatan', 'kabupaten', 'nama_kabupaten', 'provinsi', 'nama_provinsi',
            'deskripsi', 'kendala', 'kesimpulan', 'tindak_lanjut', 'dokumentasi'
        ).order_by('-tanggal_awal')
    
        serialized_data = []
        for item in data:
            serialized_item = {
                'id': item['id'],
                'status': item['status'],
                'nama_satker': item['satker__nama_satker'],
                'satker_parent_id': item['satker_id'],
                'tanggal_awal': item['tanggal_awal'],
                'tanggal_akhir': item['tanggal_akhir'],
                'desa': item['desa'],
                'nama_desa': item['nama_desa'],
                'kecamatan': item['kecamatan'],
                'nama_kecamatan': item['nama_kecamatan'],
                'kabupaten': item['kabupaten'],
                'nama_kabupaten': item['nama_kabupaten'],
                'provinsi': item['provinsi'],
                'nama_provinsi': item['nama_provinsi'],
                'deskripsi': item['deskripsi'],
                'kendala': item['kendala'],
                'kesimpulan': item['kesimpulan'],
                'tindak_lanjut': item['tindak_lanjut'],
                'dokumentasi': item['dokumentasi'],
            }
            serialized_data.append(serialized_item)

        return serialized_data
    
    @action(detail=True, methods=['delete'])
    def delete_all_kegiatan(self, request, pk=None):
        try:
            deleted_count, _ = models.DAYATIF_PEMETAAN_POTENSI.objects.filter(satker_id=pk).delete()
            
            return Response({
                'status': deleted_count > 0,
                'deleted_count' : deleted_count,
                'message': 'Data kegiatan berhasil dihapus' if deleted_count > 0 else f'Data kegiatan dari Satker ID {pk} tidak ditemukan',
                'satker_id': pk,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'status': False,
                'message': f'Gagal saat menghapus semua kegiatan pada satker_id {pk}',
                'satker_id': pk,
                'error': f'{str(e)}'
            }, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post'])
    def semua_kegiatan(self, request):
        tipe = request.data.get("tipe", 'kirim')
        satker_id = request.data.get("satker_id", None)
        nama_satker = request.data.get("nama_satker", None)
        
        try:
            satker_instance = Satker.objects.filter(nama_satker=nama_satker).first() if not satker_id else Satker.objects.filter(pk=satker_id).first()
            satker_parent = {}
            
            if satker_instance.level == 1:
                satker_parent_instance = satker_instance.parent
                satker_parent['id'] = satker_parent_instance.pk
                satker_parent['keterangan'] = satker_parent_instance.nama_satker
            elif satker_instance.level == 0:
                satker_parent['id'] = 213
                satker_parent['keterangan'] = 'BNN Pusat'
            else:
                satker_parent['id'] = 0
                satker_parent['keterangan'] = ''
                
            kegiatan = models.DAYATIF_PEMETAAN_POTENSI.objects.filter(satker_id=satker_instance.pk)

            print('Kegiatan:', len(kegiatan))
            
            message = ''
            
            if tipe == 'kirim':
                if satker_instance.level == 0:
                    kegiatan.update(status=2)
                elif satker_instance.level == 1:
                    kegiatan.update(status=1)
                    
                message = f'Data kegiatan dari Satuan Kerja {satker_instance.nama_satker} berhasil dikirim ke {satker_parent.get("keterangan")}'
            else:
                if satker_instance.level == 0:
                    kegiatan.update(status=1)
                elif satker_instance.level == 1:
                    kegiatan.update(status=0)
                
                message = f'Data kegiatan dari Satuan Kerja {satker_instance.nama_satker} berhasil dibatalkan dikirim ke {satker_parent.get("keterangan")}'
                
            return Response({
                'status': True,
                'message': message,
                'parent': satker_parent,
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'status': False,
                'message': f'Gagal melakukan proses kirim/batal dari Satuan Kerja {nama_satker or satker_id}',
                'satker': nama_satker or satker_id,
                'error': f'{str(e)}'
            }, status=status.HTTP_400_BAD_REQUEST)
    
    
    @action(detail=False, methods=['post'])
    def kirim_kegiatan(self, request):
        kegiatan_id = request.data.get("kegiatan_id", None)
        kegiatan_id = int(kegiatan_id) if kegiatan_id else kegiatan_id
        
        try:
            satker_instance = self.request.user.profile.satker
            satker_parent = {}
            
            if satker_instance.level == 1:
                satker_parent_instance = satker_instance.parent
                satker_parent['id'] = satker_parent_instance.pk
                satker_parent['keterangan'] = satker_parent_instance.nama_satker
            elif satker_instance.level == 0:
                satker_parent['id'] = 213
                satker_parent['keterangan'] = 'BNN Pusat'
            else:
                satker_parent['id'] = 0
                satker_parent['keterangan'] = ''
                
            kegiatan = models.DAYATIF_PEMETAAN_POTENSI.objects.filter(pk=kegiatan_id).first()
            
            print('Kegiatan ', kegiatan)
            
            if satker_instance.level == 0: # BNNP ke Pusat
                kegiatan.status = 2
            elif satker_instance.level == 1: # BNNK ke BNNP
                kegiatan.status = 1
            
            kegiatan.save()
                
            return Response({
                'status': True,
                'message': f'Data kegiatan ID {kegiatan_id} dari Satuan Kerja {satker_instance.nama_satker} berhasil dikirim ke {satker_parent.get("keterangan")}',
                'parent': satker_parent,
                'status_kegiatan': kegiatan.status
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'status': False,
                'message': f'Gagal mengirim kegiatan ID {kegiatan_id} dari Satuan Kerja ID {satker_instance.pk}',
                'kegiatan_id': kegiatan_id,
                'error': f'{str(e)}'
            }, status=status.HTTP_400_BAD_REQUEST)