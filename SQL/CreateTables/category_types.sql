-- Table: public.category_types

-- DROP TABLE IF EXISTS public.category_types;

CREATE TABLE IF NOT EXISTS public.category_types
(
    category_type_id smallint NOT NULL,
    category_type character varying(16) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT category_types_pkey PRIMARY KEY (category_type_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.category_types
    OWNER to postgres;

GRANT SELECT ON TABLE public.category_types TO app;

GRANT ALL ON TABLE public.category_types TO postgres;

INSERT INTO category_types(category_type_id, category_type)
    VALUES (1, 'INCOME');

INSERT INTO category_types(category_type_id, category_type)
    VALUES (2, 'FIXED_EXPENSE');

INSERT INTO category_types(category_type_id, category_type)
    VALUES (3, 'VARIABLE_EXPENSE');