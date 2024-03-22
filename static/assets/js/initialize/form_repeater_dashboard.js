$(function () {
    var n,
        o,
        e = $(".bootstrap-maxlength-example"),
        t = $(".form-repeater");
    e.length &&
        e.each(function () {
            $(this).maxlength({
                warningClass: "label label-success bg-success text-white",
                limitReachedClass: "label label-danger",
                separator: " out of ",
                preText: "You typed ",
                postText: " chars available.",
                validate: !0,
                threshold: +this.getAttribute("maxlength"),
            });
        }),
        t.length &&
        ((n = 2),
            (o = 1),
            t.on("submit", function (e) {
                e.preventDefault();
            }),
            t.repeater({
                show: function () {
                    var r = $(this).find(".form-control, .form-select"),
                        a = $(this).find(".form-label");
                    r.each(function (e) {
                        var t = "form-repeater-" + n + "-" + o;
                        $(r[e]).attr("id", t), $(a[e]).attr("for", t), o++;
                    }),
                        n++,
                        $(this).slideDown();
                },
                // hide: function (e) {
                //     confirm(
                //         "Are you sure you want to delete this element?"
                //     ) && $(this).slideUp(e);
                // },
                hide: function (e) {
                    $(this).slideUp(e);
                },
            }));
});