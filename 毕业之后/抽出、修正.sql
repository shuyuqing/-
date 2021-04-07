select * from ipossch.pt32 where DAIKANNO = '82001001325991   '
update ipossch.pt32 set DAIKANNO = '0000000000000098'where DAIKANNO = '82001001325991   ';
select * from ipossch.pt32 where DAIKANNO = '0000000000000098'
update ipossch.pt32 set PNTYUKOT = '20211006'where DAIKANNO = '0000000000000098';
update ipossch.pt32 set KIKNGSIKOP= '-230'where DAIKANNO = '0000000000000098';
###5件だけ
select * from ipossch.pt29 where rownum<5;

select * from ipossch.pt71 where PT71.YMD >= '20201101'
AND ipossch.PT71.YMD <= '20211010';

update ipossch.pt06 set car = '20211006'where DAIKANNO = '0000000000000098';

select * from ipossch.pt06 where pt06.cardno='00000133585     ' and cardsyucd='70001'
and YMD = '20200101' and HMS ='10172833 ' and TORINO = '004198585';

select * from ipossch.pt06 
where KANKAISHACD='01' 
and CARDNO='00000133585     '
and cardsyucd='70001'
and YMD = '20200101' 
and HMS ='10172833 '
and KAISHACD='1010'
and TENCD='0080'
and TERMNO='9500                '
and TORINO='004198585'
and INSSYU='001'
and TORINO = '004198585' 
and ENTHMS = '121130756'
and KSIKIN=70321
and KEIYMD='20200101'
and KEIHMS='121130756'
and CARDNOSYUCD='0000013358570001     ';


insert into ipossch.pt06(ENTYMD,ENTTERM,KANKAISHACD,CARDNO,CARDSYUCD,YMD,HMS,KAISHACD,TENCD,TERMNO,TORINO,INSSYU,ENTHMS,KSIKIN,KEIYMD,KEIHMS,CARDNOSYUCD)
                  values('20200101','','01','3911102010111111','11111','01','00000133585     ','70001','20200101','10172833 ','1010','0080','9500                ',00419858,'001','121130756','0000013358570001     ');

update ipossch.pt06 
set CARDNO='3911102010111111',CARDSYUCD = '11111'
where KANKAISHACD='01' 
and CARDNO='00000145210'
and cardsyucd='70001'
and YMD = '20200101' 
and HMS ='10093033 ' 
and KAISHACD='1010'
and TENCD='0080'
and TERMNO='9500                '
and TORINO='004198498'
and INSSYU='001'
and TORINO = '004198498' 
and ENTHMS = '121107764';

update ipossch.pt06 
set CARDNO='00000000119     ',CARDSYUCD = '11111'
where KANKAISHACD='01' 
and CARDNO='00000145210     '
and cardsyucd='70001'
and YMD = '20200101' 
and HMS ='10413333 ' 
and KAISHACD='1010'
and TENCD='0080'
and TERMNO='9500                '
and TORINO='004198745'
and INSSYU='001'
and TORINO = '004198745' 
and ENTHMS = '121221053';

select * from ipossch.PT71
where ipossch.PT71.CARDNO = '3911102010111111' AND ipossch.PT71.CARDSYUCD = '11111';

update ipossch.PT71
set YMD = '20200101'
where ipossch.PT71.CARDNO = '3911102010111111' AND ipossch.PT71.CARDSYUCD = '11111';

select * from ipossch.PT06
where CARDNO='00000000119     'and CARDSYUCD = '11111';

select * from ipossch.PT71
where ipossch.PT71.CARDNO = '3911102010111111' AND ipossch.PT71.CARDSYUCD = '11111' and pt71.HMS='10000002 ';

update ipossch.PT71
set cardno = '00000133585     ', CARDSYUCD = '70001'
where ipossch.PT71.CARDNO = '3911102010111111' AND ipossch.PT71.CARDSYUCD = '11111' and pt71.ENTHMS='170851002';

select count(*) from ipossch.ptf8;

select * from ipossch.pt91 where KANKAISHACD='01' and SHOHINKOKANID = 59917;


update ipossch.pt91 
set SHOHINCD = '51101           '
where KANKAISHACD = '01'
and SHOHINKOKANID = 59916;



update ipossch.pt91 
set UKEYMD = '20210101'
where KANKAISHACD = '01'
and SHOHINKOKANID = 59917;


select * from ipossch.pt25
where UPDYMD = '20210318' and ENTPGID = 'PNMB010M';

update ipossch.pt01 
set JTAREKNJ1 = 'ハハハハハハ'
where DAIKANNO = '0000000000000100';


select * from ipossch.pt29 where LOG_DATETIME like '%2021032919%' and UPDATE_USER_ID = 'FJSFUJITSU011';


update ipossch.pt09 
set CARDGPRYAK = 'テストGP1'
where KANKAISHACD = '01'
and CARDGPCD = '00001';

select * from ipossch.pt09
where CARDGPCD = '00001';

select count(*) from ipossch.D10
