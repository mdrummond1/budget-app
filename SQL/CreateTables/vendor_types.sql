-- Table: public.vendor_types

-- DROP TABLE IF EXISTS public.vendor_types;

CREATE TABLE IF NOT EXISTS public.vendor_types
(
    vendor_type_id SERIAL NOT NULL,
    vendor_type character varying(25) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT vendor_types_pkey PRIMARY KEY (vendor_type_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.vendor_types
    OWNER to postgres;

GRANT UPDATE, INSERT, SELECT ON TABLE public.vendor_types TO app;

GRANT ALL ON TABLE public.vendor_types TO postgres;