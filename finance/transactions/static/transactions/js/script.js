

$(document).ready(function() {
    function loadCategories(typeId, selectedCategoryId = null) {
        if (typeId) {
            $.ajax({
                url: '/ajax/load-categories/',
                data: { 'type': typeId },
                success: function(data) {
                    $('#id_category').empty();
                    $('#id_category').append('<option value="">---------</option>');
                    $.each(data, function(index, item) {
                        var selected = (selectedCategoryId == item.id) ? 'selected' : '';
                        $('#id_category').append('<option value="' + item.id + '" ' + selected + '>' + item.name + '</option>');
                    });
                    if (data.length > 0) {
                        loadSubcategories(data[0].id);
                    } else {
                        $('#id_subcategory').empty();
                        $('#id_subcategory').append('<option value="">---------</option>');
                    }
                }
            });
        } else {
            $('#id_category').empty();
            $('#id_category').append('<option value="">---------</option>');
            $('#id_subcategory').empty();
            $('#id_subcategory').append('<option value="">---------</option>');
        }
    }

    function loadSubcategories(categoryId, selectedSubcategoryId = null) {
        if (categoryId) {
            $.ajax({
                url: '/ajax/load-subcategories/',
                data: { 'category': categoryId },
                success: function(data) {
                    $('#id_subcategory').empty();
                    $('#id_subcategory').append('<option value="">---------</option>');
                    $.each(data, function(index, item) {
                        var selected = (selectedSubcategoryId == item.id) ? 'selected' : '';
                        $('#id_subcategory').append('<option value="' + item.id + '" ' + selected + '>' + item.name + '</option>');
                    });
                }
            });
        } else {
            $('#id_subcategory').empty();
            $('#id_subcategory').append('<option value="">---------</option>');
        }
    }

    // Event listener for type change
    $('#id_type').change(function() {
        var typeId = $(this).val();
        loadCategories(typeId);
    });

    // Event listener for category change
    $('#id_category').change(function() {
        var categoryId = $(this).val();
        loadSubcategories(categoryId);
    });

    // Initialize on page load if values are already selected (for edit forms)
    var initialTypeId = $('#id_type').val();
    var initialCategoryId = $('#id_category').val();
    var initialSubcategoryId = $('#id_subcategory').val();

    if (initialTypeId) {
        loadCategories(initialTypeId, initialCategoryId);
    }
    if (initialCategoryId) {
        loadSubcategories(initialCategoryId, initialSubcategoryId);
    }
});
