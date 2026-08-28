football_team_project.py

Proyecto desarrollado como práctica de **Programación Orientada a Objetos** 
usando equipos de fútbol como contexto.

## Descripción

Sistema de gestión de equipos de fútbol que implementa los conceptos 
fundamentales de POO: herencia, encapsulamiento, abstracción y polimorfismo.


## Estructura del Proyecto

Football/
├── Player.py → Clase jugador con goles, transferencias y retiro
├── Coach.py → Clase entrenador con instrucciones tácticas
├── FootballTeam.py → Clase equipo base con jugadores y entrenador
├── ClubTeam.py → Hereda de FootballTeam, agrega trofeos y estadio
├── League.py → Clase liga con clasificación de equipos
├── Match.py → Clase partido con simulación de resultado
├── Stadium.py → Clase estadio vinculado al equipo
└── Main.py → Punto de entrada del programa

## Conceptos POO Aplicados

| Concepto | Dónde se aplica |
|---|---|
| **Herencia** | `ClubTeam` hereda de `FootballTeam` |
| **Encapsulamiento** | Atributos protegidos con `self` en cada clase |
| **Abstracción** | Cada clase representa una entidad del mundo real |
| **Polimorfismo** | `sign_player` y `add_player` logran lo mismo de forma diferente |


## Cómo ejecutar

1. Clona el repositorio:
```bash
git clone https://github.com/tuusuario/Football-POO.git
```

2. Entra a la carpeta:
```bash
cd Football-POO
```

3. Ejecuta el Main:
```bash
python Main.py
```

##  Retos implementados

| Reto | Descripción |
|---|---|
| Challenge 1 | Clase `Player` con atributos y método `score` |
| Challenge 2 | Método `transfer` en `Player` |
| Challenge 3 | Clase `Coach` con método `give_instructions` |
| Challenge 4 | Método `hire_coach` en `FootballTeam` |
| Challenge 5 | Clase `League` con clasificación |
| Challenge 6 | Método `sign_player` en `ClubTeam` |
| Challenge 7 | Clase `Match` con simulación de partido |
| Challenge 8 | Comparación de equipos por trofeos |
| Challenge 9 | Clase `Stadium` vinculada a `ClubTeam` |
| Challenge 10 | Método `retire` en `Player` |


## 👤 Autor

**Sebastian David Rodriguez Urbano** 
**Andres Cardozo Daza**
**Andres Felipe Quintero**
**Andres Felipe Martinez**
Universidad de San Buenaventura  
Programación Orientada a Objetos — 2026
