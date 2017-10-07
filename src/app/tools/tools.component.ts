import { Component, OnInit } from '@angular/core';
// import { HttpClient } from '@angular/common/http';

import { ToolsService } from './tools.service';
import { Tools } from './tools';

@Component({
  selector: 'app-tools',
  templateUrl: './tools.component.html',
  styleUrls: ['./tools.component.css'],
  providers: [ToolsService]
})
export class ToolsComponent implements OnInit {

  toolsList: Tools[];

  constructor(private toolsService: ToolsService){}

  ngOnInit() {
    this.toolsService.getTools()
    .subscribe(
      data => {
        this.toolsList = data;
        console.log(data);
      },
      err => {
        console.error(err);
      })
  }

}
