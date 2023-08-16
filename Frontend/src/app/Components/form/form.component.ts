import { Component } from '@angular/core';
import { NgForm } from '@angular/forms';
import { PhonesService } from 'src/app/Services/phones.service';

@Component({
  selector: 'app-form',
  templateUrl: './form.component.html',
  styleUrls: ['./form.component.css']
})
export class FormComponent {
  constructor(public phonesServise :PhonesService) {}
  addPhone(form:NgForm){
    this.phonesServise.addPhone(form.value).subscribe(
      res=>{
        form.reset();
        this.phonesServise.getCelAll().subscribe(
          res => {
            this.phonesServise.celulares = res;
            console.log(res)
          },
          err => console.error(err)
        )
      },
      err=> console.error(err)
    )
  }
  putPhone(form:NgForm){
    this.phonesServise.updatePhone(form.value).subscribe(
      res=>{
        this.phonesServise.update=false;
        form.reset();
        this.phonesServise.getCelAll().subscribe(
          res => {
            this.phonesServise.celulares = res;
            console.log(res)
          },
          err => console.error(err)
        )
      },
      err=> console.error(err)
    )
  }

}
