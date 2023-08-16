import { HttpClient } from '@angular/common/http'
import { Injectable } from '@angular/core';
import { Phone, Phone2 } from '../Models/Phone';
import { format } from 'date-fns'

@Injectable({
  providedIn: 'root'
})
export class PhonesService {
  /* 2 */
  URLWEB = 'http://127.0.0.1:8000/';
  celulares : Phone[]=[];

  selectCel:Phone2={
    idPh:123,
    Marca:"",
    AndroidVersion:"",
    Ram:2,
    Almacenamiento:16,
    Estado:true,
    FechaActualizacion:format(new Date(), 'yyyy-MM-dd hh:mm:ss')
  }
  update:boolean=false;
  constructor(private http: HttpClient) { }
  /* 3 */
  getCelAll(){
    return this.http.get<Phone[]>(this.URLWEB+'phone/get_All')
  }
  /*  */
  addPhone(phone:Phone){
    return this.http.post(this.URLWEB+'phone/insert',phone)
  }
  /*  */
  deletePhone (id:Number){
    return this.http.delete(this.URLWEB+'phone/delete/'+id)
  }
  /*  */
  updatePhone(phone:Phone){
    return this.http.put(this.URLWEB+'phone/update/'+phone.idPh,phone)
  }
}
