$(document).ready(function(){
    $('.add-comment').each(function(){
        elem = $(this)

        elem.click(function(){
            show_add_comment($(this).parent(), $(this).parent().children('input').val()); 
        });
    });
});


function show_add_comment(parent, post_id){
    csrf_html = parent.find("input[name='csrfmiddlewaretoken']").parent().html()
    parent.html('\
    <form action="/comment/new/' + post_id + '/" method="post">            \
        ' + csrf_html + ' \
        <div><textarea name="text" rows="2" cols="50"></textarea></div>            \
        <div><input type="submit" value="Add Comment"></div>        \
    </form>            \
    '    
    )
}