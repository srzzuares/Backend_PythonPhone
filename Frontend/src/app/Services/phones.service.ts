import { HttpClient } from '@angular/common/http'
import { Injectable } from '@angular/core';
import { Phone, Phone2 } from '../Models/Phone';

@Injectable({
  providedIn: 'root'
})
export class PhonesService {
  /* 2 */
  URLWEB = 'http://127.0.0.1:8000/';
  celulares : Phone[]=[];

  selecCel:Phone2={
    Marca:"",
    AndroidVersion:"",
    Ram:2,
    Almacenamiento:16,
    Estado:true
  }
  constructor(private http: HttpClient) { }
  /* 3 */
  getCelAll(){
    return this.http.get<Phone[]>(this.URLWEB+'phone/get_All')
  }
}
