import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class QuizsService {
  userLoginStatus=false;
  constructor(private hc:HttpClient ) {}

  getData():Observable<any>{
    return this.hc.get<any>("http://127.0.0.1:8800/auth/")
  }

  createUser(userObj):Observable<any>{
    return this.hc.post("http://127.0.0.1:8800/auth/register/student/",userObj)
  }

  loginUser(credentials):Observable<any>{
    return this.hc.post("http://127.0.0.1:8800/auth/login/",credentials)
  }
  
}
