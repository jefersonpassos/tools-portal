import { Component, OnInit } from '@angular/core';

import { ToolsService } from './tools.service';

@Component({
  selector: 'app-tools',
  templateUrl: './tools.component.html',
  styleUrls: ['./tools.component.css']
})
export class ToolsComponent implements OnInit {


  toolsList:any[];
  
  toolsService = new ToolsService(); 

  constructor(){
    this.toolsList = this.toolsService.getTools();
  }

  ngOnInit() {
  }

}
