-- Database generated with pgModeler (PostgreSQL Database Modeler).
-- pgModeler  version: 0.9.2
-- PostgreSQL version: 12.0
-- Project Site: pgmodeler.io
-- Model Author: ---


-- Database creation must be done outside a multicommand file.
-- These commands were put in this file only as a convenience.
-- -- object: new_database | type: DATABASE --
-- -- DROP DATABASE IF EXISTS new_database;
-- CREATE DATABASE new_database;
-- -- ddl-end --
-- 

-- object: public."Usuario" | type: TABLE --
-- DROP TABLE IF EXISTS public."Usuario" CASCADE;
CREATE TABLE public."Usuario" (
	"Correo" varchar(100) NOT NULL,
	"Nombre" varchar(45) NOT NULL,
	"Apellido" varchar(45) NOT NULL,
	edad integer NOT NULL,
	peso float NOT NULL,
	estatura integer NOT NULL,
	"contraseña" varchar(50) NOT NULL,
	"Id_Genero" integer,
	CONSTRAINT "Usuario_pk" PRIMARY KEY ("Correo")

);
-- ddl-end --
-- ALTER TABLE public."Usuario" OWNER TO postgres;
-- ddl-end --

-- object: public."Genero" | type: TABLE --
-- DROP TABLE IF EXISTS public."Genero" CASCADE;
CREATE TABLE public."Genero" (
	"Id" serial NOT NULL,
	"Nombre" varchar(45),
	CONSTRAINT "Genero_pk" PRIMARY KEY ("Id")

);
-- ddl-end --
-- ALTER TABLE public."Genero" OWNER TO postgres;
-- ddl-end --

-- object: "Genero_fk" | type: CONSTRAINT --
-- ALTER TABLE public."Usuario" DROP CONSTRAINT IF EXISTS "Genero_fk" CASCADE;
ALTER TABLE public."Usuario" ADD CONSTRAINT "Genero_fk" FOREIGN KEY ("Id_Genero")
REFERENCES public."Genero" ("Id") MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: public."Pulsioximetro" | type: TABLE --
-- DROP TABLE IF EXISTS public."Pulsioximetro" CASCADE;
CREATE TABLE public."Pulsioximetro" (
	fecha timestamp NOT NULL,
	pulso integer,
	oxigeno integer,
	"Correo_Usuario" varchar(100) NOT NULL,
	CONSTRAINT "Pulsioximetro_pk" PRIMARY KEY (fecha,"Correo_Usuario")

);
-- ddl-end --
-- ALTER TABLE public."Pulsioximetro" OWNER TO postgres;
-- ddl-end --

-- object: "Usuario_fk" | type: CONSTRAINT --
-- ALTER TABLE public."Pulsioximetro" DROP CONSTRAINT IF EXISTS "Usuario_fk" CASCADE;
ALTER TABLE public."Pulsioximetro" ADD CONSTRAINT "Usuario_fk" FOREIGN KEY ("Correo_Usuario")
REFERENCES public."Usuario" ("Correo") MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: public."Acelerometro" | type: TABLE --
-- DROP TABLE IF EXISTS public."Acelerometro" CASCADE;
CREATE TABLE public."Acelerometro" (
	fecha timestamp NOT NULL,
	gx float,
	gy float,
	gz float,
	"Correo_Usuario" varchar(100) NOT NULL,
	CONSTRAINT "Acelerometro_pk" PRIMARY KEY (fecha,"Correo_Usuario")

);
-- ddl-end --
-- ALTER TABLE public."Acelerometro" OWNER TO postgres;
-- ddl-end --

-- object: "Usuario_fk" | type: CONSTRAINT --
-- ALTER TABLE public."Acelerometro" DROP CONSTRAINT IF EXISTS "Usuario_fk" CASCADE;
ALTER TABLE public."Acelerometro" ADD CONSTRAINT "Usuario_fk" FOREIGN KEY ("Correo_Usuario")
REFERENCES public."Usuario" ("Correo") MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: public."Notificaciones" | type: TABLE --
-- DROP TABLE IF EXISTS public."Notificaciones" CASCADE;
CREATE TABLE public."Notificaciones" (
	fecha timestamp NOT NULL,
	mensaje varchar(100),
	"Correo_Usuario" varchar(100) NOT NULL,
	CONSTRAINT "Notificaciones_pk" PRIMARY KEY (fecha,"Correo_Usuario")

);
-- ddl-end --
-- ALTER TABLE public."Notificaciones" OWNER TO postgres;
-- ddl-end --

-- object: "Usuario_fk" | type: CONSTRAINT --
-- ALTER TABLE public."Notificaciones" DROP CONSTRAINT IF EXISTS "Usuario_fk" CASCADE;
ALTER TABLE public."Notificaciones" ADD CONSTRAINT "Usuario_fk" FOREIGN KEY ("Correo_Usuario")
REFERENCES public."Usuario" ("Correo") MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --


