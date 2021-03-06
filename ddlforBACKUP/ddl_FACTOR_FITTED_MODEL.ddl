--------------------------------------------------------
--  DDL for Table FACTOR_FITTED_MODEL
--------------------------------------------------------

  CREATE TABLE "IF_A2RPT"."FACTOR_FITTED_MODEL" 
   (	"FITTED_MODEL_SK" NUMBER, 
	"VARIABLE_SK" NUMBER, 
	"FROM_DT" DATE, 
	"TO_DT" DATE, 
	"FITTED_DT" DATE, 
	"SELECTED_FLG" VARCHAR2(1 BYTE), 
	"HIDDEN_FLG" VARCHAR2(1 BYTE), 
	"FIT_DATA" CLOB, 
	"MODEL_DESCRIPTION" VARCHAR2(2000 BYTE)
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "INTERFACE" 
 LOB ("FIT_DATA") STORE AS BASICFILE (
  TABLESPACE "INTERFACE" ENABLE STORAGE IN ROW CHUNK 8192 RETENTION 
  NOCACHE LOGGING 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)) ;
REM INSERTING into IF_A2RPT.FACTOR_FITTED_MODEL
SET DEFINE OFF;
Insert into IF_A2RPT.FACTOR_FITTED_MODEL (FITTED_MODEL_SK,VARIABLE_SK,FROM_DT,TO_DT,FITTED_DT,SELECTED_FLG,HIDDEN_FLG,MODEL_DESCRIPTION) values (552,146,to_date('11-JUL-07','DD-MON-RR'),to_date('13-JUL-17','DD-MON-RR'),to_date('13-JUL-17','DD-MON-RR'),'N','N',null);
Insert into IF_A2RPT.FACTOR_FITTED_MODEL (FITTED_MODEL_SK,VARIABLE_SK,FROM_DT,TO_DT,FITTED_DT,SELECTED_FLG,HIDDEN_FLG,MODEL_DESCRIPTION) values (547,146,to_date('01-MAY-06','DD-MON-RR'),to_date('01-MAY-16','DD-MON-RR'),to_date('07-JUL-17','DD-MON-RR'),'N','N',null);
Insert into IF_A2RPT.FACTOR_FITTED_MODEL (FITTED_MODEL_SK,VARIABLE_SK,FROM_DT,TO_DT,FITTED_DT,SELECTED_FLG,HIDDEN_FLG,MODEL_DESCRIPTION) values (553,122,to_date('01-MAY-06','DD-MON-RR'),to_date('01-MAY-16','DD-MON-RR'),to_date('13-JUL-17','DD-MON-RR'),'Y','N',null);
Insert into IF_A2RPT.FACTOR_FITTED_MODEL (FITTED_MODEL_SK,VARIABLE_SK,FROM_DT,TO_DT,FITTED_DT,SELECTED_FLG,HIDDEN_FLG,MODEL_DESCRIPTION) values (550,146,to_date('15-JUL-09','DD-MON-RR'),to_date('21-JUL-16','DD-MON-RR'),to_date('13-JUL-17','DD-MON-RR'),'N','N',null);
Insert into IF_A2RPT.FACTOR_FITTED_MODEL (FITTED_MODEL_SK,VARIABLE_SK,FROM_DT,TO_DT,FITTED_DT,SELECTED_FLG,HIDDEN_FLG,MODEL_DESCRIPTION) values (546,146,to_date('01-MAY-06','DD-MON-RR'),to_date('01-MAY-16','DD-MON-RR'),to_date('07-JUL-17','DD-MON-RR'),'N','N',null);
Insert into IF_A2RPT.FACTOR_FITTED_MODEL (FITTED_MODEL_SK,VARIABLE_SK,FROM_DT,TO_DT,FITTED_DT,SELECTED_FLG,HIDDEN_FLG,MODEL_DESCRIPTION) values (551,146,to_date('09-JUL-08','DD-MON-RR'),to_date('13-JUL-17','DD-MON-RR'),to_date('13-JUL-17','DD-MON-RR'),'N','N',null);
Insert into IF_A2RPT.FACTOR_FITTED_MODEL (FITTED_MODEL_SK,VARIABLE_SK,FROM_DT,TO_DT,FITTED_DT,SELECTED_FLG,HIDDEN_FLG,MODEL_DESCRIPTION) values (541,146,to_date('01-JAN-10','DD-MON-RR'),to_date('28-APR-17','DD-MON-RR'),to_date('06-JUL-17','DD-MON-RR'),'N','Y',null);
Insert into IF_A2RPT.FACTOR_FITTED_MODEL (FITTED_MODEL_SK,VARIABLE_SK,FROM_DT,TO_DT,FITTED_DT,SELECTED_FLG,HIDDEN_FLG,MODEL_DESCRIPTION) values (548,146,to_date('01-MAY-06','DD-MON-RR'),to_date('01-MAY-16','DD-MON-RR'),to_date('07-JUL-17','DD-MON-RR'),'Y','N',null);
--------------------------------------------------------
--  DDL for Index FACTOR_FITTED_MODEL_PK
--------------------------------------------------------

  CREATE UNIQUE INDEX "IF_A2RPT"."FACTOR_FITTED_MODEL_PK" ON "IF_A2RPT"."FACTOR_FITTED_MODEL" ("FITTED_MODEL_SK") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "INTERFACE" ;
--------------------------------------------------------
--  DDL for Index FACTOR_FITTED_MODEL_INDEX1
--------------------------------------------------------

  CREATE INDEX "IF_A2RPT"."FACTOR_FITTED_MODEL_INDEX1" ON "IF_A2RPT"."FACTOR_FITTED_MODEL" ("VARIABLE_SK") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "INTERFACE" ;
--------------------------------------------------------
--  DDL for Trigger FACTOR_FITTED_MODEL_TRG
--------------------------------------------------------

  CREATE OR REPLACE TRIGGER "IF_A2RPT"."FACTOR_FITTED_MODEL_TRG" 
BEFORE INSERT ON FACTOR_FITTED_MODEL 
FOR EACH ROW 
BEGIN
  <<COLUMN_SEQUENCES>>
  BEGIN
    IF INSERTING AND :NEW.FITTED_MODEL_SK IS NULL THEN
      SELECT FACTOR_FITTED_MODEL_SEQ.NEXTVAL INTO :NEW.FITTED_MODEL_SK FROM SYS.DUAL;
    END IF;
  END COLUMN_SEQUENCES;
END;
/
ALTER TRIGGER "IF_A2RPT"."FACTOR_FITTED_MODEL_TRG" ENABLE;
--------------------------------------------------------
--  Constraints for Table FACTOR_FITTED_MODEL
--------------------------------------------------------

  ALTER TABLE "IF_A2RPT"."FACTOR_FITTED_MODEL" ADD CONSTRAINT "FACTOR_FITTED_MODEL_PK" PRIMARY KEY ("FITTED_MODEL_SK")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "INTERFACE"  ENABLE;
  ALTER TABLE "IF_A2RPT"."FACTOR_FITTED_MODEL" MODIFY ("VARIABLE_SK" NOT NULL ENABLE);
  ALTER TABLE "IF_A2RPT"."FACTOR_FITTED_MODEL" MODIFY ("FITTED_MODEL_SK" NOT NULL ENABLE);
