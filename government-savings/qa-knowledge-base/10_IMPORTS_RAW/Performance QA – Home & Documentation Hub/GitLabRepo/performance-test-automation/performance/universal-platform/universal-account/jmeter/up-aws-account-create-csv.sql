select memberID, uii_acct_id, ownerID
from (
    select distinct 
        lower(regexp_replace(m.uuid_member_id, '(.{8})(.{4})(.{4})(.{4})(.{12})', '\1-\2-\3-\4-\5')) memberID, 
        a.uii_acct_id, 
        lower(regexp_replace(p.uuid_person_id, '(.{8})(.{4})(.{4})(.{4})(.{12})', '\1-\2-\3-\4-\5')) ownerID,
        ROW_NUMBER() OVER (PARTITION BY a.traunch_id ORDER BY a.uii_acct_id) as rn
    from tu_acct a, tu_member m, tu_person p, tu_traunch t
    where a.traunch_id in ('100066', '100009', '100080', '100081', '100049')
    and m.web_registered = 'Y'
    and a.acct_state = '91'
    and a.uii_acct_ext = '01'
    and a.uii_member_id = m.uii_member_id
    and a.seq_part_id = p.seq_person_id
    and a.traunch_id = t.traunch_id
) ranked
where rn <= 20;
