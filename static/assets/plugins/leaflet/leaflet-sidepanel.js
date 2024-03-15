/**
 * @name Leaflet.SidePanel
 * @link https://github.com/maxwell-ilai/Leaflet.SidePanel
 */

L.Control.SidePanel=L.Control.extend({includes:L.Evented.prototype,options:{panelPosition:"left",hasTabs:!0,tabsPosition:"top",darkMode:!1,pushControls:!1,startTab:1},initialize:function(t,o){this._panel=L.DomUtil.get(t),L.setOptions(this,o)},addTo:function(t){L.DomUtil.addClass(this._panel,"sidepanel-"+this.options.panelPosition),this.options.darkMode&&L.DomUtil.addClass(this._panel,"sidepanel-dark"),L.DomEvent.disableScrollPropagation(this._panel),L.DomEvent.disableClickPropagation(this._panel),this.options.hasTabs&&this.initTabs(t,this.options.tabsPosition)},initTabs:function(t,o){"string"==typeof o&&L.DomUtil.addClass(this._panel,"tabs-"+o);let s=this._panel.querySelectorAll("a.sidebar-tab-link"),e=this._panel.querySelectorAll(".sidepanel-tab-content");s.forEach(function(t,o){let i,a;"number"==typeof this.options.startTab&&this.options.startTab-1===o&&(i=t,a=e[o-1]),"string"==typeof this.options.startTab&&this.options.startTab===t.dataset.tabLink&&(i=t,a=this._panel.querySelector(`.sidepanel-tab-content[data-tab-content="${this.options.startTab}"]`)),void 0===i||L.DomUtil.hasClass(i,"active")||(L.DomUtil.addClass(i,"active"),L.DomUtil.addClass(a,"active")),L.DomEvent.on(t,"click",function(o){if(L.DomEvent.preventDefault(o),!L.DomUtil.hasClass(t,"active")){for(let t=0;t<s.length;t++){let o=s[t];L.DomUtil.hasClass(o,"active")&&L.DomUtil.removeClass(o,"active")}L.DomUtil.addClass(t,"active"),e.forEach(function(o){t.dataset.tabLink===o.dataset.tabContent?L.DomUtil.addClass(o,"active"):L.DomUtil.removeClass(o,"active")})}},t)}.bind(this)),this._toggleButton(t)},_toggleButton:function(t){const o=this._panel.querySelector(".sidepanel-toggle-container"),s=o.querySelector(".sidepanel-toggle-button");L.DomEvent.on(s,"click",function(o){let s=!0,e=L.DomUtil.hasClass(this._panel,"opened"),i=L.DomUtil.hasClass(this._panel,"closed");if(e||i?!e&&i?(L.DomUtil.addClass(this._panel,"opened"),L.DomUtil.removeClass(this._panel,"closed")):e&&!i?(s=!1,L.DomUtil.removeClass(this._panel,"opened"),L.DomUtil.addClass(this._panel,"closed")):L.DomUtil.addClass(this._panel,"opened"):L.DomUtil.addClass(this._panel,"opened"),this.options.pushControls){let o=t.getContainer().querySelector(".leaflet-control-container");L.DomUtil.addClass(o,"leaflet-anim-control-container"),s?(L.DomUtil.removeClass(o,this.options.panelPosition+"-closed"),L.DomUtil.addClass(o,this.options.panelPosition+"-opened")):(L.DomUtil.removeClass(o,this.options.panelPosition+"-opened"),L.DomUtil.addClass(o,this.options.panelPosition+"-closed"))}}.bind(this),o)}}),L.control.sidepanel=function(t,o){return new L.Control.SidePanel(t,o)};