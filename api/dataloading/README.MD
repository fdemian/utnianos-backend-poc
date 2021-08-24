# Carga de datos.

La carga de datos se hace llamando al programa `modcp` con dos parametros:
  - command: el programa a ejecutar. Determina el tipo de archivo que se va a cargar.
  - file: el archivo desde donde se cargan los datos.

## Cargar planes de carrera.

### Comando para la carga de datos.

```
python3 modcp.py --command CareerPlans --file <path/to/career plans>/career_plans.json
```

### Formato del JSON.

```
[
  {
    "name": "",
    "code": ""
  }
]
```

Donde

  - name: representa el nombre (legible por humanos) de la materia.
  - code: representa el codigo de materia.

Por ejemplo, para ingenieria en sistemas, esto sería:

```
{
  "name": "Ingeniería en sistemas de Información [K08] (UTN - FRBA)",
  "code": "K08"
}
```

## Cargar cursadas.

1) Cargar todos los cursos de una cursada.

```
python3 modcp.py --command Courses --file <path/to/<courses>/courses.json
```

```
[
  {
    "code": "",
    "name": "",
    "year": 1
  }
]
```

Siendo:
  - code: código único de la materia.
  - name: nómbre de la materia.
  - year: año al que pertenece la materia.

2) Cargar la asociación entre materias y cursadas.

Esto es necesario porque hay materias que se comparten entre varias cursadas, por lo cual una materia puede asociarse a dos carreras distintas (por ejemplo, las materias básicas).

```
python3 modcp.py --command CourseAssociations --file  <path/to/<course by career>/courses_ing_sist.json
```

Formato del JSON:

```
{
  "code": "K08-INT",
  "courses": [""]
}
```

Donde

  - code: codigo único de la carrera.
  - courses: lista de codigos de materia que pertenecen a esa carrera.

Por ejemplo:

```
{
  "code": "K08-INT",
  "courses": [
    "950702",
    "950701",
    "082020",
    "082021",
    "082022"
  ]
}
```

## Cargar correlativas de materias.

```
python3 modcp.py --command Prerrequisites --file <path to prerequisites>/correlativas_analista_sistemas.json
```

```
[{
	"code": "",
	"courseRequisites": [{
			"code": "",
			"status": ""
		}
	],
	"finalRequisites": [{
			"code": "",
			"status": ""
		}
	]
}]
```

Donde

  - code: código de la materia.
  - courseRequisites: requisitos para cursar la materia. Array compuesto por
     + code: código de la materia correlativa.
     + status: estado de la materia, siendo uno de C (se require haberla cursado) ó F (se require tener final de la materia).
  - finalRequisites: requisitos para dar final. Array compuesto por
     + code: código de la materia correlativa.
     + status: estado de la materia, siendo uno de C (se require haberla cursado) ó F (se require tener final de la materia).

Por ejemplo (correlativas de Análisis de Sistemas):

```
[{
		"code": "082024",
		"courseRequisites": [{
				"code": "082023",
				"status": "C"
			},
			{
				"code": "082021",
				"status": "C"
			}
		],
		"finalRequisites": [{
				"code": "082023",
				"status": "F"
			},
			{
				"code": "082021",
				"status": "F"
			}
		]
	}
]
```
