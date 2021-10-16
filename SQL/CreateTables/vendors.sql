-- Table: public.vendors

-- DROP TABLE IF EXISTS public.vendors;

CREATE TABLE IF NOT EXISTS public.vendors
(
    vendor_id SERIAL NOT NULL,
    vendor_type integer,
    name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    web_address character varying(255) COLLATE pg_catalog."default",
    CONSTRAINT vendors_pkey PRIMARY KEY (vendor_id),
    CONSTRAINT vendors_vendor_type_fkey FOREIGN KEY (vendor_type)
        REFERENCES public.vendor_types (vendor_type_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.vendors
    OWNER to postgres;

GRANT UPDATE, INSERT, SELECT ON TABLE public.vendors TO app;

GRANT ALL ON TABLE public.vendors TO postgres;