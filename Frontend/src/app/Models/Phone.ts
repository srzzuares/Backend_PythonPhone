/* 1.-Modelo */

export interface Phone {
    idPh:Number
    Marca: String
    AndroidVersion: String
    Ram: Number
    Almacenamiento: Number
    Estado:Boolean
    FechaActualizacion:Date
    FechaRegistro:Date
}

export interface Phone2 {
    Marca: String
    AndroidVersion: String
    Ram: Number
    Almacenamiento: Number
    Estado:Boolean
}