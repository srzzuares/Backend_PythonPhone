import { Component } from '@angular/core';
import { PhonesService } from 'src/app/Services/phones.service';


@Component({
  selector: 'app-table',
  templateUrl: './table.component.html',
  styleUrls: ['./table.component.css']
})
export class TableComponent {
  constructor(public phonesService: PhonesService) { }
  ngOnInit() {
    this.getAllStudents();
  }
  getAllStudents() {
    this.phonesService.getCelAll().subscribe(
      res => {
        this.phonesService.celulares = res;
        console.log(res)
      },
      err => console.error(err)
    )
  }
}
