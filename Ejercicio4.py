import os
class Empleado:
    def __init__(self,CC,nombre,departamento,puesto,salariomin):
        self.CC=CC
        self.nombre=nombre
        self.departamento=departamento
        self.puesto=puesto
        self.salariomin=salariomin

class Controlador:
    CC=[]
    nombre=[]
    departamento=[]
    puesto=[]
    sueldo=[]
    
    def __init__(self):
        self.interfaz()
        
    def interfaz(self):
        while True:
            print("----------------------------------")
            print("-Gestion de Empleados-")
            print("1- Agregar empleado. ")
            print("2- Asignar tarea. ")
            print("3- Calcular salario. ")
            print("4- Generar informe. ")
            print("5- Mostrar empleados. ")
            print("0- Salir. ")
            opcion=int(input("-"))
            
            if opcion == 1:
                empl1=Departamento(None,None,None,None,None)
                empl1.AgregarEmpleado()
            elif opcion == 2:
                empl2=Tarea()
                empl2.AsignarTarea()
            elif opcion == 3:
                empl3=Departamento()
                empl3.CalcularSalario()
            elif opcion == 4:
                empl4=Departamento()
                empl4.GenerarInforme()
            elif opcion == 5:
                empl5=Tarea()
                empl5.MostrarEmpleados()
            elif opcion == 0:
                break
            input()
            os.system("cls")

class Tarea(Empleado):

    def __init__(self):
        pass

    def AsignarTarea(self):
        pass
        
    def MostrarEmpleados(self):
        if len(Controlador.nombre) != 0:
            for empleado in Controlador.nombre:
                print(empleado)
        else:
            print("No hay empleados registrados")

class Departamento(Empleado):

    def __init__(self):
        pass

    def AgregarEmpleado(self):
        self.CC=int(input("Ingrese la cedula del empleado: "))
        Controlador.CC.append(self.CC)
        self.nombre=input("Ingrese el nombre del empleado: ")
        Controlador.nombre.append(self.nombre)
        self.departamento=input("Ingrese el departamento: ")
        Controlador.departamento.append(self.departamento)
        self.puesto=input("Ingrese el puesto: ")
        Controlador.puesto.append(self.puesto)
        print("Empleado registrado con exito")

    def CalcularSalario(self):
        if len(Controlador.CC) != 0:
            if 
            self.salariomin=float(input("Ingrese el salario minimo mensual: "))
            self.comision=float(input("Ingrese el valor de la comision mensual: "))
            self.sueldo=self.salariomin+self.comision
            Controlador.sueldo.append(self.sueldo)
            print("Se registro el salario del empleado")
        else:
            print("No hay empleados registrados")

    def GenerarInforme(self):
        if len(Controlador.CC) != 0:
            print("------------------------------------------------------------------------")
            print("                       Reporte de empleados    ")
            print("------------------------------------------------------------------------")
            print("Cedula          Nombre          Departamento          Puesto          Sueldo")
            for i in range (len(Controlador.CC)):
                print(f"{Controlador.CC[i]:0,.0f}                 {Controlador.nombre[i]}              {Controlador.departamento[i]}                {Controlador.puesto[i]}                {Controlador.sueldo[i]:0,.3f}")
            print(f"Total: {len(Controlador.CC)} empleados")
        else:
            print("No hay empleados registrados")

proyecto=Controlador()