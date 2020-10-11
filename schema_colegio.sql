-- Database: sistema_colegio

-- DROP DATABASE sistema_colegio;

CREATE DATABASE sistema_colegio
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Spanish_Peru.1252'
    LC_CTYPE = 'Spanish_Peru.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

-- TABLAS
-- alumnos

-- Table: public.alumnos

-- DROP TABLE public.alumnos;

CREATE TABLE public.alumnos
(
    alumno_id SERIAL, --('alumnos_alumno_id_seq'::regclass),
    nombres character varying(150) COLLATE pg_catalog."default",
    edad integer,
    correo character varying(150) COLLATE pg_catalog."default",
    CONSTRAINT alumnos_pkey PRIMARY KEY (alumno_id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.alumnos
    OWNER to postgres;

-- cursos

-- Table: public.cursos

-- DROP TABLE public.cursos;

CREATE TABLE public.cursos
(
    curso_id SERIAL, --('cursos_curso_id_seq'::regclass),
    nombre character varying(150) COLLATE pg_catalog."default",
    CONSTRAINT cursos_pkey PRIMARY KEY (curso_id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.cursos
    OWNER to postgres;

-- malla_curricular
-- Table: public.malla_curricular

-- DROP TABLE public.malla_curricular;

CREATE TABLE public.malla_curricular
(
    id_malla SERIAL, --('malla_curricular_id_malla_seq'::regclass),
    id_periodo integer NOT NULL,
    id_salon integer NOT NULL,
    id_profesor_curso integer NOT NULL,
    CONSTRAINT malla_curricular_pkey PRIMARY KEY (id_malla)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.malla_curricular
    OWNER to postgres;

-- notas

-- Table: public.notas

-- DROP TABLE public.notas;

CREATE TABLE public.notas
(
    id_nota SERIAL, --('notas_id_nota_seq'::regclass),
    id_alumno integer NOT NULL,
    id_malla integer NOT NULL,
    nota double precision NOT NULL,
    CONSTRAINT notas_pkey PRIMARY KEY (id_nota)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.notas
    OWNER to postgres;

-- periodo_escolar

-- Table: public.periodo_escolar

-- DROP TABLE public.periodo_escolar;

CREATE TABLE public.periodo_escolar
(
    id_periodo SERIAL, --('periodo_escolar_id_periodo_seq'::regclass),
    nombre_periodo character varying(150) COLLATE pg_catalog."default",
    fecha_desde date,
    fecha_hasta date,
    CONSTRAINT periodo_escolar_pkey PRIMARY KEY (id_periodo)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.periodo_escolar
    OWNER to postgres;

-- profesor_curso

-- Table: public.profesor_curso

-- DROP TABLE public.profesor_curso;

CREATE TABLE public.profesor_curso
(
    id_profesor_curso SERIAL, --('profesor_curso_id_profesor_curso_seq'::regclass),
    id_profesor integer NOT NULL,
    id_curso integer NOT NULL,
    CONSTRAINT profesor_curso_pkey PRIMARY KEY (id_profesor_curso)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.profesor_curso
    OWNER to postgres;

-- profesores

-- Table: public.profesores

-- DROP TABLE public.profesores;

CREATE TABLE public.profesores
(
    profesor_id SERIAL, --('profesores_profesor_id_seq'::regclass),
    nombres character varying(150) COLLATE pg_catalog."default",
    edad integer,
    correo character varying(150) COLLATE pg_catalog."default",
    CONSTRAINT profesores_pkey PRIMARY KEY (profesor_id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.profesores
    OWNER to postgres;

-- salones

-- Table: public.salones

-- DROP TABLE public.salones;

CREATE TABLE public.salones
(
    id_salon SERIAL, --('salones_id_salon_seq'::regclass),
    nombre_salon character varying(150) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT salones_pkey PRIMARY KEY (id_salon)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.salones
    OWNER to postgres;