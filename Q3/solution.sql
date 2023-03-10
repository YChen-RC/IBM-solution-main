select a.owner_id as owner_id, o.owner_name as owner_name, count(distinct category_id) as different_category_count
from article as a
         right join owner as o
              on o.owner_id = a.owner_id
         join category_article_mapping as c
              on c.article_id = a.article_id
group by a.owner_id
order by count(distinct category_id) asc;
