# Reqs

## Us

Como usuario, quiero generar todos los archivos necesarios para mi ci vendor para incorporar ci a mi proyecto
Como usuario, quiero que el sistema tome como configuracion la especificacion centralizada del proyecto
	- Quiero que el sistema tome la configuracion de CI
		- Valores de aceptacion de calidad de codigo y demas
	- Quiero que el sistema tome la configuracion del proyecto para los entornos de ejecucion
Como usuario, quiero decidir bajo que eventos si y no desencadenar las ejecuciones de cada stage
Como usuario, quiero decidir que pasos si y no incluir para mi pipeline
Como usuario, quiero generar todos los archivos necesarios para mi vcs para incorporar ci a mi proyecto
Como usuario, quiero poder especificar y usar diferentes ci vendors (como gh actions) para tener portabilidad

## Quality attrs

1. Apertura (a utilizar en un futuro otros vendors, otros formatos de configuracion...)
2. Informacion (necesito conocer todo lo posible lo antes posible)

## Features

- CI files-per-vendor generation
	- Use Github actions as CI vendor
- On-Demand Pipeline Generator
	- Select what stages to include in
	- Select what stage steps to include in
	- Select Stage trigger setter

## Notes

Sobre #TDD: El hook de pre-commit debe permitir cuestiones de baja calidad del codigo, no errores. Permitibles incluyen:
	0. Al menos los siguientes valores de pylint: 20, 4 y 16
	1. Sugerencias de refactor
	2. Sugerencias por estandares
	3. Sugerencias de warnings
Sin embargo SI deberia mostrar esa informacion, para agilizar el diseño entre commits.
Sobre #Entornos: El sistema de CI puede estar distribuido entre local y centralizado (o clientes y servidores del vcs usado). 
Por eso, el sistema generaodr debe permitir la creacion de ambos. Tanto un pipe en cliente, probablemente usando hooks 
para el pre commit, como la centralizacion de todo el pipeline en github.
