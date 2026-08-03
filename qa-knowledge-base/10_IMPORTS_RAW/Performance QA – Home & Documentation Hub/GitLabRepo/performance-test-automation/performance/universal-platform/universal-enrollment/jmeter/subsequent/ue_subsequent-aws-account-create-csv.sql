select tf.traunch_id, f.fund_id
from tu_traunch_fund tf, tu_funds f
where tf.traunch_id = '100066'
and tf.ctl_rec_stat = 'A'
and f.web_status = 'A'
and f.back_status = 'A'
and f.fund_id = tf.fund_id
and rownum < 4;

select distinct lower(regexp_replace(m.uuid_member_id, '(.{8})(.{4})(.{4})(.{4})(.{12})', '\1-\2-\3-\4-\5')) memberID, a.uii_acct_id, 
lower(regexp_replace(p.uuid_person_id, '(.{8})(.{4})(.{4})(.{4})(.{12})', '\1-\2-\3-\4-\5')) ownerID, 
lower(regexp_replace(t.uuid_traunch_id, '(.{8})(.{4})(.{4})(.{4})(.{12})', '\1-\2-\3-\4-\5')) planId, t.branding, '1066001', '1066002', '1066003'
from tu_acct a, tu_member m, tu_person p, tu_traunch t
where a.traunch_id = '100066'
and m.web_registered = 'Y'
and a.acct_state = '91'
and a.uii_acct_ext = '01'
and a.uii_member_id = m.uii_member_id
and a.seq_part_id = p.seq_person_id
and a.traunch_id = t.traunch_id;
