### Taller de índices

# -------- 1

# -------- a --------

USE familias_en_accion; 

SET GLOBAL local_infile = 1;
DROP TABLE IF EXISTS beneficiarios_familias_accion;
CREATE TABLE beneficiarios_familias_accion (
    Bancarizado VARCHAR(5), 
    CodigoDepartamentoAtencion INT, 
    CodigoMunicipioAtencion INT, 
    Discapacidad VARCHAR(5), 
    EstadoBeneficiario VARCHAR(20), 
    Etnia VARCHAR(50), 
    FechaInscripcionBeneficiario DATE, 
    Genero VARCHAR(10), 
    NivelEscolaridad VARCHAR(50), 
    NombreDepartamentoAtencion VARCHAR(100), 
    NombreMunicipioAtencion VARCHAR(100), 
    Pais VARCHAR(50), 
    TipoAsignacionBeneficio VARCHAR(50), 
    TipoBeneficio VARCHAR(50), 
    TipoDocumento VARCHAR(10), 
    TipoPoblacion VARCHAR(50), 
    RangoBeneficioConsolidadoAsignado VARCHAR(50), 
    RangoUltimoBeneficioAsignado VARCHAR(50), 
    FechaUltimoBeneficioAsignado DATE, 
    RangoEdad VARCHAR(20), 
    Titular VARCHAR(5), 
    CantidadDeBeneficiarios INT 
);
LOAD DATA LOCAL INFILE "C:/Users/nicol/Downloads/Beneficiarios_M_s_Familias_en_Acci_n_20250620.csv" 
INTO TABLE beneficiarios_familias_accion
FIELDS TERMINATED BY ','      
IGNORE 1 ROWS                
;

SELECT COUNT(*) FROM beneficiarios_familias_accion;		-- Verificar el número de filas

# -------- b --------
-- Seleccionar todos los campos de la tabla cuando TipoPoblacion sea “Desplazado”
SELECT *
FROM beneficiarios_familias_accion
WHERE TipoPoblacion = 'DESPLAZADOS';

-- Seleccionar todos los campos de la tabla que hayan tenido su último beneficio después de 01/01/2018
SELECT *
FROM beneficiarios_familias_accion
WHERE FechaUltimoBeneficioAsignado > '2018-01-01';

# -------- 2

# -------- a --------
CREATE INDEX idx_tipo_poblacion
ON beneficiarios_familias_accion (TipoPoblacion);

# -------- b --------
CREATE INDEX idx_fecha_ultimo_beneficio
ON beneficiarios_familias_accion (FechaUltimoBeneficioAsignado);

# -------- c --------
-- Nuevamente hacer las consultas realizadas en el punto 1

# -------- 3
CREATE TABLE empleado (emple_id INT NOT NULL PRIMARY KEY,
nombre VARCHAR(10),
edad INT,
sexo CHAR(1),
INDEX ind_nombre (nombre)
);

DESCRIBE empleado;

# -------- 4
ALTER TABLE empleado
DROP INDEX ind_nombre;

# -------- 5

# -------- a --------
ALTER TABLE empleado
ADD INDEX idx_edad (edad);

# -------- b --------
ALTER TABLE empleado
DROP INDEX idx_edad;

# -------- 6

# -------- a --------
CREATE UNIQUE INDEX idx_edad_unique
ON empleado (edad);

# -------- b --------
ALTER TABLE empleado
DROP INDEX idx_edad_unique;

# -------- 7

# -------- a --------
CREATE TABLE lookup (id INT, INDEX (id) USING BTREE);

# -------- 8

CREATE TABLE autor (			-- Crear primero la tabla
    autor_id INT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50)
);

CREATE UNIQUE INDEX idx_apellido_unique
ON autor (apellido)
USING BTREE;

DESCRIBE autor;