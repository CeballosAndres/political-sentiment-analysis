-- Store proc for clear all data related with a page
CREATE PROCEDURE delete_all_page_data(IN page_name varchar(255))
BEGIN
    DELETE FROM comment WHERE post_id IN
        (SELECT id FROM post WHERE post.page_id IN
            (SELECT id FROM page WHERE page.page_name=page_name));

    DELETE FROM post WHERE post.page_id IN
        (SELECT id FROM page WHERE page.page_name=page_name);

    DELETE FROM page WHERE page.page_name=page_name;
END;