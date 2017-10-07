import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';


import { Tools } from './tools';
import { TOOLS } from './mock-tools';

@Injectable()
export class ToolsService {

  apiUrl = "http://127.0.0.1:8000/api";

  constructor(private http:HttpClient) { }

  getTools(){
      return this.http.get<Tools[]>(this.apiUrl + '/tools/');
  }

  ngOnInit() {

  }

  private handleError(error: any): Promise<any> {
    console.error('An error occurred', error); // for demo purposes only
    return Promise.reject(error.message || error);
  }


}
