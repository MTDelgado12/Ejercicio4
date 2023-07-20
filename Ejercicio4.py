import os
empleados=[]
class Empleado:
    def __init__(self, CC, nombre, departamento, puesto, salariomin):
        self.CC = CC
        self.nombre = nombre
        self.departamento = departamento
        self.puesto = puesto
        self.salariomin = salariomin or 0.0
        self.comision = 0.0
        self.tarea = None

class Controlador:
    def __init__(self):
        self.interfaz()
        
    def interfaz(self):
        while True:
            print("----------------------------------")
            print("-Gestion de Empleados-")
            print("1- Agregar empleado. ")
            print("2- Asignar tarea. ")
            print("3- Mostrar tareas. ")
            print("4- Calcular salario. ")
            print("5- Generar informe. ")
            print("6- Mostrar empleados. ")
            print("7- Mostrar tareas asignadas. ")
            print("0- Salir. ")
            opcion=int(input("-"))
            
            if opcion == 1:
                empl1=Departamento()
                empl1.AgregarEmpleado()
            elif opcion == 2:
                empl2=Tarea()
                empl2.AsignarTarea()
            elif opcion == 3:
                empl3=Tarea()
                empl3.MostrarTarea()
            elif opcion == 4:
                empl4=Departamento()
                empl4.CalcularSalario()
            elif opcion == 5:
                empl5=Departamento()
                empl5.GenerarInforme()
            elif opcion == 6:
                empl6=Tarea()
                empl6.MostrarEmpleados()
            elif opcion == 7:
                empl7=Tarea()
                empl7.MostrarTareasAsignadas()
            elif opcion == 0:
                break
            input()
            os.system("cls")

class Tarea(Empleado):
    tareas= ["Administrar recursos",
            "Realizar informes",
            "Entregar proyecto",
            "Verificar informe"]

    def __init__(self):
        pass                      
        
    def MostrarEmpleados(self):
        if len(empleados) != 0:
            for indice, empleado in enumerate(empleados, start=1):
                print(f"Número: {indice}")
                print("Cédula:", empleado.CC)
                print("Nombre:", empleado.nombre)
                print("Departamento:", empleado.departamento)
                print("Puesto:", empleado.puesto)
                print("------------------------")
        else:
            print("No hay empleados registrados")

    def MostrarTarea(self):
        print("Tareas: ")
        for i in range (len(Tarea.tareas)):
            print(f"{i+1}- {Tarea.tareas[i]}")

    def AsignarTarea(self):
        if len(empleados) != 0:
            self.MostrarEmpleados()
            self.MostrarTarea()
            indice = int(input("Ingrese el indice del empleado al que desea asignarle la tarea: "))
            if 1 <= indice <= len(empleados):
                if empleados[indice - 1].tarea == None:
                    empleado = empleados[indice- 1]
                    empleado.tarea = int(input("Ingrese el número de la tarea que desea asignar: "))
                    print("Se asignó la tarea al empleado")
                else:
                    print("El empleado ya tiene una tarea asignada")
        else:
            print("No hay empleados registrados")

    def MostrarTareasAsignadas(self):
        if len(empleados) != 0:
            for indice, empleado in enumerate(empleados, start=1):
                print(f"Número: {indice}")
                print("Nombre:", empleado.nombre)
                print("Departamento:", empleado.departamento)
                print("Tarea:", empleado.tarea)
                print("------------------------")
        else:
            print("No hay empleados registrados o no hay tareas asignadas")

class Departamento(Empleado):

    def __init__(self):
        pass

    def AgregarEmpleado(self):
        self.CC=int(input("Ingrese la cedula del empleado: "))
        self.nombre=input("Ingrese el nombre del empleado: ")
        self.departamento=input("Ingrese el departamento: ")
        self.puesto=input("Ingrese el puesto: ")
        empleados.append(Empleado(self.CC,self.nombre,self.departamento,self.puesto,None))
        print("Empleado registrado con exito")

    def CalcularSalario(self):
        if len(empleados) != 0:
            tarea = Tarea()
            tarea.MostrarEmpleados()
            seleccion = int(input("Ingrese el número del empleado que desea actualizar el salario: "))
            if  1 <=  seleccion <= len(empleados):
                empleado = empleados[seleccion - 1]
                empleado.salariomin = float(input("Ingrese el salario mínimo mensual: "))
                empleado.comision = float(input("Ingrese el valor de la comisión mensual: "))
                empleado.salariomin += empleado.comision
                print("Se actualizó el salario del empleado")
            else:
                print("Número de empleado inválido")
        else:
            print("No hay empleados registrados")

    def GenerarInforme(self):
        if len(empleados) != 0:
            print("--------------------------------------------------------------------------------------")
            print("                       Reporte de empleados    ")
            print("--------------------------------------------------------------------------------------")
            print("Cedula            Nombre              Departamento                 Puesto                     Sueldo")
            for empleado in empleados:
                print(f"{empleado.CC}             {empleado.nombre}                  {empleado.departamento}                {empleado.puesto}                  s        {empleado.salariomin}")
            print(f"Total: {len(empleados)} empleados")
        else:
            print("No hay empleados registrados")

proyecto=Controlador()