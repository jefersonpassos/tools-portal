import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';

import { ToolsComponent } from './tools.component';


@NgModule({
  imports: [
    CommonModule,
    HttpClientModule
  ],
  declarations: [ToolsComponent],
  exports: [ToolsComponent]
})
export class ToolsModule { }
