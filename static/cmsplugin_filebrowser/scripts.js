/*global $, mhajax */
var cmsplugin_filebrowser = (function () {
    'use strict';

    var
        $filebrowser,
        $cwd,
        $list,
        $file_template,
        $folder_template,
        $up;

    function populateListGroup(data) {

        $list.children('.list-group-item:not(.template)').remove();

        $cwd.text(data.path);

        $up.data('parent-path', data.parent_path);

        data.fileinfos.forEach(
            function (fileinfo) {
                var $template;
                if (fileinfo.is_folder) {
                    $template = $folder_template;
                } else {
                    $template = $file_template;
                }
                $template
                    .clone(true, true)
                    .appendTo($list)
                    .removeClass('template')
                    .removeClass('hidden')
                    .data('fileinfo', fileinfo)
                    .text(fileinfo.name);
            }
        );
    }

    function loadListing(url) {

        mhajax.get_json(url).done(
            function (data) {
                populateListGroup(data);
            }
        );
    }

    function callback_ClickListItem(event) {
        loadListing($(event.delegateTarget).data('fileinfo').link);
    }

    return {
        init: function (starting_url) {

            $filebrowser = $('div.filebrowser');
            $cwd = $filebrowser.find('.filebrowser-cwd');
            $list = $filebrowser.find('.filebrowser-list');

            $up = $filebrowser.find('.filebrowser-up');
            $up.click(
                function () {
                    loadListing($up.data('parent-path'));
                }
            );

            $file_template = $list.children('.filebrowser-item-file');
            $folder_template = $list.children('.filebrowser-item-folder');

            $list
                .children('.list-group-item')
                .click(callback_ClickListItem);

            loadListing(starting_url);
        }
    };
}());
