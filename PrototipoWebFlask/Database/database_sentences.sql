-- Database generated with pgModeler (PostgreSQL Database Modeler).
-- pgModeler  version: 0.9.2
-- PostgreSQL version: 12.0
-- Project Site: pgmodeler.io
-- Model Author: ---


-- Database creation must be done outside a multicommand file.
-- These commands were put in this file only as a convenience.
-- -- object: new_database | type: DATABASE --
-- -- DROP DATABASE IF EXISTS new_database;
-- CREATE DATABASE Cornerstone;
-- -- ddl-end --
-- 

-- object: public.Usuario | type: TABLE --
-- DROP TABLE IF EXISTS public.Usuario CASCADE;
CREATE TABLE public.Usuario (
	Correo varchar(100) NOT NULL,
	Nombre varchar(45) NOT NULL,
	Apellido varchar(45) NOT NULL,
	edad integer NOT NULL,
	peso float NOT NULL,
	estatura integer NOT NULL,
	contraseña varchar(50) NOT NULL,
	Id_Genero integer,
	CONSTRAINT Usuario_pk PRIMARY KEY (Correo)

);
-- ddl-end --
-- ALTER TABLE public.Usuario OWNER TO postgres;
-- ddl-end --

-- object: public.Genero | type: TABLE --
-- DROP TABLE IF EXISTS public.Genero CASCADE;
CREATE TABLE public.Genero (
	Id serial NOT NULL,
	Nombre varchar(45),
	CONSTRAINT Genero_pk PRIMARY KEY (Id)

);
-- ddl-end --
-- ALTER TABLE public.Genero OWNER TO postgres;
-- ddl-end --

-- object: Genero_fk | type: CONSTRAINT --
-- ALTER TABLE public.Usuario DROP CONSTRAINT IF EXISTS Genero_fk CASCADE;
ALTER TABLE public.Usuario ADD CONSTRAINT Genero_fk FOREIGN KEY (Id_Genero)
REFERENCES public.Genero (Id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: public.Pulsometro | type: TABLE --
-- DROP TABLE IF EXISTS public.Pulsometro CASCADE;
CREATE TABLE public.Pulsometro (
	fecha timestamp NOT NULL,
	pulso integer,
	Correo_Usuario varchar(100) NOT NULL,
	CONSTRAINT Pulsiometro_pk PRIMARY KEY (fecha,Correo_Usuario)

);
-- ddl-end --
-- ALTER TABLE public.Pulsometro OWNER TO postgres;
-- ddl-end --

-- object: Usuario_fk | type: CONSTRAINT --
-- ALTER TABLE public.Pulsometro DROP CONSTRAINT IF EXISTS Usuario_fk CASCADE;
ALTER TABLE public.Pulsometro ADD CONSTRAINT Usuario_fk FOREIGN KEY (Correo_Usuario)
REFERENCES public.Usuario (Correo) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: public.Acelerometro | type: TABLE --
-- DROP TABLE IF EXISTS public.Acelerometro CASCADE;
CREATE TABLE public.Acelerometro (
	fecha timestamp NOT NULL,
	gx float,
	gy float,
	gz float,
	Correo_Usuario varchar(100) NOT NULL,
	CONSTRAINT Acelerometro_pk PRIMARY KEY (fecha,Correo_Usuario)

);
-- ddl-end --
-- ALTER TABLE public.Acelerometro OWNER TO postgres;
-- ddl-end --

-- object: Usuario_fk | type: CONSTRAINT --
-- ALTER TABLE public.Acelerometro DROP CONSTRAINT IF EXISTS Usuario_fk CASCADE;
ALTER TABLE public.Acelerometro ADD CONSTRAINT Usuario_fk FOREIGN KEY (Correo_Usuario)
REFERENCES public.Usuario (Correo) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: public.Notificaciones | type: TABLE --
-- DROP TABLE IF EXISTS public.Notificaciones CASCADE;
CREATE TABLE public.Notificaciones (
	fecha timestamp NOT NULL,
	mensaje varchar(100),
	Correo_Usuario varchar(100) NOT NULL,
	CONSTRAINT Notificaciones_pk PRIMARY KEY (fecha,Correo_Usuario)

);
-- ddl-end --
-- ALTER TABLE public.Notificaciones OWNER TO postgres;
-- ddl-end --

-- object: Usuario_fk | type: CONSTRAINT --
-- ALTER TABLE public.Notificaciones DROP CONSTRAINT IF EXISTS Usuario_fk CASCADE;
ALTER TABLE public.Notificaciones ADD CONSTRAINT Usuario_fk FOREIGN KEY (Correo_Usuario)
REFERENCES public.Usuario (Correo) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

--Añadir columnas necesarias para calcular el porcentaje de actividad física


ALTER TABLE pulsometro ADD porcentaje_activdad NUMERIC NULL;

ALTER TABLE usuario ADD ritmo_basal INT NULL;

ALTER TABLE usuario ADD reserva NUMERIC NULL;

--Añadir géneros en tabla género

INSERT INTO genero VALUES(0, 'mujer');
INSERT INTO genero VALUES(1, 'hombre');

--TRIGGER FUNCTIONS

DROP FUNCTION IF EXISTS RRC_mujer() CASCADE;

CREATE OR REPLACE FUNCTION RRC_mujer()
	RETURNS TRIGGER
	AS 
		$$ 
		begin	
			UPDATE usuario
			SET reserva = (214-usuario.edad*0.8)-usuario.ritmo_basal
			WHERE correo = NEW.correo AND id_genero = 0;
			RETURN NEW;
		end;
		$$
	LANGUAGE plpgsql;
	
CREATE TRIGGER RRC_mujer
	AFTER INSERT
	ON usuario
	FOR EACH ROW
	EXECUTE PROCEDURE RRC_mujer();

DROP FUNCTION IF EXISTS RRC_hombre() CASCADE;

CREATE OR REPLACE FUNCTION RRC_hombre()
	RETURNS TRIGGER
	AS 
		$$ 
		begin	
			UPDATE usuario
			SET reserva = (209-usuario.edad*0.7)-usuario.ritmo_basal
			WHERE correo = NEW.correo AND id_genero = 1;
			RETURN NEW;
		end;
		$$
	LANGUAGE plpgsql;
	
CREATE TRIGGER RRC_hombre
	AFTER INSERT
	ON usuario
	FOR EACH ROW
	EXECUTE PROCEDURE RRC_hombre();

DROP FUNCTION IF EXISTS karvonen() CASCADE;

CREATE OR REPLACE FUNCTION karvonen()
	RETURNS TRIGGER
	AS 
		$$
		declare
			basal integer;
			rrc numeric;
		begin	
			SELECT ritmo_basal into basal
			FROM usuario, pulsometro
			WHERE pulso = NEW.pulso AND correo = correo_usuario;
			
			SELECT reserva into rrc
			FROM usuario, pulsometro
			WHERE pulso = NEW.pulso AND correo = correo_usuario;
			
			UPDATE pulsometro
			SET porcentaje_activdad = (pulso - basal)/rrc
			WHERE fecha = NEW.fecha;
			RETURN NEW;
		end;
		$$
	LANGUAGE plpgsql;
	
CREATE TRIGGER karvonen
	AFTER INSERT
	ON pulsometro
	FOR EACH ROW
	EXECUTE PROCEDURE karvonen();


