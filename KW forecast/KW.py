from datetime import *
from time import *


input_kw = raw_input('enter your KW:   ').lower()
kw_list = input_kw.split(',')
kw_query = ''
kw_total_query = ''
input_date_begin = raw_input('Enter begin date, format ''YYYY-MM-DD''  : ')
input_date_end = raw_input('Enter end date, format ''YYYY-MM-DD'' : ')


for item in kw_list:

     kw_query+=  " OR (lower(t1.Video_Tags)) like '% " + item.strip() + " %'" 
     kw_query+=  " OR (lower(t1.Video_Title)) like '% " + item.strip() + " %'" 
     kw_query+=  " OR (lower(t1.Video_description)) like '% " + item.strip() + " %'" 

     kw_query+=  " OR (lower(t1.Video_Tags)) like '% " + item.strip() + "'" 
     kw_query+=  " OR (lower(t1.Video_Title)) like '% " + item.strip() + "'" 
     kw_query+=  " OR (lower(t1.Video_description)) like '% " + item.strip() + "'" 

     kw_query+=  " OR (lower(t1.Video_Tags)) like '" + item.strip() + " %'" 
     kw_query+=  " OR (lower(t1.Video_Title)) like '" + item.strip() + " %'" 
     kw_query+=  " OR (lower(t1.Video_description)) like '" + item.strip() + " %'" 

kw_query = kw_query[4:]



## Concatente 

kw_total_query += """
	select 
	month(date) as "Month",
	'O&O' as "Inventory",
	t3.Group_name as "Syndicator",
	t4.titile as "Category",
	sum(t2.video_views) as "Video Views",
	sum(t2.matched_views) as "Matched Views" from dwh.dim_videos t1
	left join dwh.billing_revenue t2 on t1.video_id = t2.video_id
	left join dwh.dim_groups t3 on t2.publisher_id = t3.groupid
	left join dwh.dim_channels t4 on t1.first_category_id = t4.category_id

	where ( 
     """
kw_total_query+= kw_query
kw_total_query+= """

 )

and t2.date between
"""

kw_total_query+= input_date_begin + ' and ' + input_date_end + ' '

kw_total_query+="""

and t2.country_code = 'us' and t2.publisher_id = 577
and t1.member_id not in 
(
select member_id from dwh.billing_revenue where content_owner_id in (
1625,
1064,
1256,
1294,
195,
536,
991,
696,
1414,
1766,
1018,
1182,
1047,
1978,
273,
543
 )
)

and t1.member_id not in (
517229271,
517229272,
518005517,
517791313,
517936933,
517229273,
517741276,
517394847,
518038264,
517484515,
517394850,
518020716,
517186676,
517436728,
517750750,
517181726,
517877107,
517990437,
518018512,
517742769,
517887470,
517953113,
517951318,
517895248,
517971997,
517999193,
517976308,
518024576,
517118627,
517989654,
517883187,
517964399,
517825764,
517765601,
517825816,
517522665,
517369459,
517939650,
518027096,
517830392,
517802283,
517112012,
517738144,
517687056,
517658220,
517631386,
518034120,
516983004,
517767612,
517394905,
517657691,
517775071,
517917258,
517711200,
517787224,
517715430,
517690116,
517852581,
517896704,
517893681,
517887462,
517887469,
517426923,
517631423,
517719900,
517425613,
517696791,
517297702,
517725277,
517718700,
517425767,
517935103,
517965064,
517964523,
517970214,
518012214,
518049995,
518052263,
518038264,
518087073,
517394850,
518122690,
518095410,
518130942,
518130944,
518076539,
518076545,
518078385,
518093822,
518093790,
517369459,
518136996,
518130942,
517765601,
518107917,
518137554,
517394847,
517484515,
518173906,
518173907,
518178605,
518241776,
518238427,
518214622,
518237172,
518272379,
227248886,
518255551,
518344180,
518294563,
518252715,
518275913,
518256025,
518285988,
518319510,
518364780,
518357668,
518155490,
518240118
)

group by t3.group_name,month(date),t4.titile


--Combine Two parts
UNION ALL

--Forecast for Network
select 
month(date) as "Month",
'Network' as "Inventory",
t3.Group_name as "Syndicator",
t4.titile as "Category",
sum(t2.video_views) as "Video Views",
sum(t2.matched_views) as "Matched Views" from dwh.dim_videos t1
left join dwh.billing_revenue t2 on t1.video_id = t2.video_id
left join dwh.dim_groups t3 on t2.publisher_id = t3.groupid
left join dwh.dim_channels t4 on t1.first_category_id = t4.category_id

where (
"""
kw_total_query+= kw_query
kw_total_query+= """

 )

and t2.date between
"""

kw_total_query+= input_date_begin + ' and ' + input_date_end + ' '

kw_total_query+="""

and t2.country_code = 'us' and t2.publisher_id != 577
and t2.publisher_id != 670 and t2.publisher_id !=954 and t2.publisher_id !=1158 and t2.publisher_id !=1863 and t2.publisher_id !=1131 
and t1.member_id not in 
(
select member_id from dwh.billing_revenue where content_owner_id in (
157,
195,
273,
536,
543,
581,
696,
764,
836,
873,
885,
948,
991,
1010,
1014,
1018,
1020,
1047,
1050,
1064,
1076,
1105,
1109,
1123,
1124,
1126,
1173,
1182,
1223,
1225,
1236,
1241,
1256,
1294,
1298,
1308,
1319,
1330,
1331,
1339,
1369,
1414,
1424,
1549,
1575,
1625,
1654,
1693,
1707,
1766,
1890,
1978
 )
)

and t1.member_id not in (
517895248,
517971997,
517999193,
517181726,
517976308,
518024576,
517118627,
517989654,
517883187,
517964399,
517825764,
517765601,
517825816,
517522665,
517369459,
517939650,
518027096,
517830392,
517802283,
518005517,
518020716,
517112012,
517738144,
517687056,
517658220,
517631386,
518034120,
516983004,
517767612,
517394905,
517657691,
517775071,
517917258,
517711200,
517787224,
517715430,
517690116,
517852581,
517896704,
517893681,
517887462,
517887469,
517426923,
517631423,
517719900,
517425613,
517696791,
517297702,
517725277,
517718700,
517425767,
517935103,
517965064,
517964523,
517970214,
518012214,
518049995,
518052263,
518038264,
518087073,
517394850,
518122690,
518095410,
518130942,
518130944,
518076539,
518076545,
518078385,
518093822,
518093790,
517369459,
518136996,
518130942,
517765601,
518107917,
518137554,
517484515,
517394847,
518173906,
518173907,
518178605,
518241776,
518238427,
518214622,
518237172,
518272379,
227248886,
518255551,
518344180,
518294563,
518252715,
518275913,
518256025,
518285988,
518319510,
518364780,
518357668,
518155490,
518240118
)

group by t3.group_name,month(date),t4.titile

"""

Output_address = 'C:/Users/zhli14/Desktop/AOL/KW forcast/KW code/' + datetime.today().strftime('%Y.%m.%d') + ' KW forecast code for '+ kw_list[0] + ' Date from ' + input_date_begin + ' to ' +input_date_end + '.txt'

file = open(Output_address,'w')
file.write(kw_total_query)
file.close()



