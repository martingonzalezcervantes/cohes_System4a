from coches import coches
from tkinter import *
from tkinter import messagebox

class App:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Gestion de coches")
        self.ventana.geometry("800x600")
        self.ventana.resizable(0,0)
        self.main()
        
    def borrarPantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    #VISTAS DEL SISTEMA   
    def menu_acciones(self):
        self.borrarPantalla()
        tipo="Coches"
        Label(self.ventana,text=f"\n...::: menu de {tipo} :::... \n")
        Button(self.ventana,text="1.- Agregar",command=self.insertar_view).pack(pady=5)
        Button(self.ventana,text="2.- Borra",command=self.eliminar_view).pack(pady=5)
        Button(self.ventana,text="3.- Modificar",command=self.modificar_view).pack(pady=5)
        Button(self.ventana,text="4.- Mostrar",command=self.consultar_view).pack(pady=5)
        Button(self.ventana,text="5.- Salir",command=self.main).pack(pady=5)
        
    def main (self):
        self.borrarPantalla()
        Label(self.ventana,text="\n...::: M E N U   P R I N C I P A L :::...").pack(pady=10)
        Button(self.ventana,text="1.- Coches",command=self.menu_acciones).pack(pady=5)
        Button(self.ventana,text="2.- Salir",command=self.ventana.quit).pack(pady=5)

    def insertar_view(self):
        self.borrarPantalla()
        Label(self.ventana,text="...Ingresar los datos de Coche").pack(pady=10)
        Label(self.ventana,text="Marca").pack(pady=5)
        self._marca=Entry(self.ventana)
        self._marca.focus()
        self._marca.pack(pady=5)
        
        Label(self.ventana,text="Color").pack(pady=5)
        self._color=Entry(self.ventana)
        self._color.pack(pady=5)
        
        Label(self.ventana,text="Modelo").pack(pady=5)
        self._modelo=Entry(self.ventana)
        self._modelo.pack(pady=5)
        
        Label(self.ventana,text="Velocidad").pack(pady=5)
        self._velocidad=Entry(self.ventana)
        self._velocidad.pack(pady=5)
        
        Label(self.ventana,text="Potencia").pack(pady=5)
        self._potencia=Entry(self.ventana)
        self._potencia.pack(pady=5)
        
        Label(self.ventana,text="Asientos").pack(pady=5)
        self._asientos=Entry(self.ventana)
        self._asientos.pack(pady=5)
        
        Button(self.ventana,text="Guardar",command=self.insertar_controller).pack(pady=10)
        Button(self.ventana,text="Regresar",command=self.menu_acciones).pack(pady=10)
        
    def eliminar_view(self):
        self.borrarPantalla()
        Label(self.ventana,text="...Ingresar el ID del Coche a eliminar").pack(pady=10)
            
        Label(self.ventana,text="ID").pack(pady=5)
        self.id=Entry(self.ventana)
        self.id.pack(pady=5)
            
            
        Button(self.ventana,text="Eliminar",command=self.eliminar_controller).pack(pady=10)
        Button(self.ventana,text="Regresar",command=self.menu_acciones).pack(pady=10)  
        
    def modificar_view(self):
            self.borrarPantalla()
            Label(self.ventana,text="...Ingresar el ID del Coche a modificar").pack(pady=10)
                    
            Label(self.ventana,text="ID").pack(pady=5)
            self.id=Entry(self.ventana)
            self.id.focus()
            self.id.pack(pady=5)
            
            Label(self.ventana,text="Nueva Marca").pack(pady=5)
            self._marca=Entry(self.ventana)
            self._marca.pack(pady=5)
                    
            Label(self.ventana,text="Nuevo Color").pack(pady=5)
            self._color=Entry(self.ventana)
            self._color.pack(pady=5)
                    
            Label(self.ventana,text="Nuevo Modelo").pack(pady=5)
            self._modelo=Entry(self.ventana)
            self._modelo.pack(pady=5)
                    
            Label(self.ventana,text="Nuevo Velocidad").pack(pady=5)
            self._velocidad=Entry(self.ventana)
            self._velocidad.pack(pady=5)
                    
            Label(self.ventana,text="Nueva Potencia").pack(pady=5)
            self._potencia=Entry(self.ventana)
            self._potencia.pack(pady=5)
                    
            Label(self.ventana,text="Nuevos Asientos").pack(pady=5)
            self._asientos=Entry(self.ventana)
            self._asientos.pack(pady=5)
                    
            Button(self.ventana,text="Guardar",command=self.modificar_controller).pack(pady=10)
            Button(self.ventana,text="Regresar",command=self.menu_acciones).pack(pady=10)
        
    def consultar_view(self):
        self.borrarPantalla()
        Label(self.ventana,text="::: Consultar los coches :::").pack(pady=10)
        filas=""
        filas=self.consultar_controller(filas)
        Label(self.ventana,text=f"{'No.':<20}{'ID':<20}{'Marca':<20}{'Color':<20}{'Modelo':<20}{'Velocidad':<20}{'Potencia':<20}{'Asientos':<20}").pack(pady=5)
        Label(self.ventana,text=f"-"*100).pack(pady=5)
        Label(self.ventana,text=f"{filas}").pack(pady=5)
        Label(self.ventana,text=f"-"*100).pack(pady=5)
        Button(self.ventana,text="Regresar",command=self.menu_acciones).pack(pady=5)
        
    
    #CONTROLADOR DEL SISTEMA
    def insertar_controller(self):
        coche1=coches.Coches(self._marca.get(),self._color.get(),self._modelo.get(),self._velocidad.get(),self._potencia.get(),self._asientos.get())
        respuesta=coche1.insertar()
        self.respuesta_sql(respuesta)
        del coche1
    
    def eliminar_controller(self):
            id=self.id.get()
            respuesta=coches.Coches.eliminar(id)
            self.respuesta_sql(respuesta)
            
    def consultar_controller(self,filas):
        registros= coches.Coches.consultar()
        if len(registros)>0:
            num_coches=1
            for fila in registros:
                filas=filas+f"\n{num_coches:<20}{fila[0]:<20}{fila[1]:<20}{fila[2]:<20}{fila[3]:<20}{fila[4]:<20}{fila[5]:<20}\{fila[6]:<20}"
                num_coches+=1
        else:
                print("\n\n\t ¡No existen datos que mostrarpor el momento ...!")
                
        return filas
    
     
    def respuesta_sql(self,respuesta):
        if respuesta:
            messagebox.showinfo(title="... Exitoso ...",message="... ¡Accion Realizada con Exito!")
        else:
            messagebox.showerror(title="...¡ Verifique por favo !...",message="...¡Esta Accion no pudo realizarse en este momento!...")
            
    def modificar_controller(self):
        id=self.id.get()
        coche1=coches.Coches(self._marca.get(),self._color.get(),self._modelo.get(),self._velocidad.get(),self._potencia.get(),self._asientos.get())
        respuesta=coche1.actualizar(id)
        self.respuesta_sql(respuesta)
        del coche1
    
                  

if __name__=="__main__":
    ventana=Tk()
    app=App(ventana)
    ventana.mainloop()
    
    

