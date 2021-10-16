-- Table: public.transaction_types

-- DROP TABLE IF EXISTS public.transaction_types;

CREATE TABLE IF NOT EXISTS public.transaction_types
(
    transaction_type_id smallint NOT NULL,
    transaction_type character varying(6) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT transaction_types_pkey PRIMARY KEY (transaction_type_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.transaction_types
    OWNER to postgres;

GRANT SELECT ON TABLE public.transaction_types TO app;

GRANT ALL ON TABLE public.transaction_types TO postgres;

INSERT INTO transaction_types(transaction_type_id, transaction_type)
    VALUES (1, "CREDIT");

INSERT INTO transaction_types(transaction_type_id, transaction_type)
    VALUES (2, "DEBIT");