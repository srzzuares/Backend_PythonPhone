import { Component } from '@angular/core';
import { Phone, Phone2 } from 'src/app/Models/Phone';
import { PhonesService } from 'src/app/Services/phones.service';


@Component({
  selector: 'app-table',
  templateUrl: './table.component.html',
  styleUrls: ['./table.component.css']
})
export class TableComponent {
  constructor(public phonesService: PhonesService) { }
  ngOnInit() {
    this.getAllPhones();
  }
  getAllPhones() {
    this.phonesService.getCelAll().subscribe(
      res => {
        this.phonesService.celulares = res;
        console.log(res)
      },
      err => console.error(err)
    )
  }
  /*  */
  deletePhone(id:Number){
    this.phonesService.deletePhone(id).subscribe(
      res => this.getAllPhones(),
      err=>console.error(err)
    )
  }
  /*  */
  getPhoneOne(celular:Phone){
    this.phonesService.selectCel=celular
    this.phonesService.update=true;
  }
}
