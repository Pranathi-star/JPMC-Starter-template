import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { QuizsService } from '../quizs.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  constructor(private qs:QuizsService,private rObj:Router) { }

  ngOnInit(): void {
  }

  onLogin(credentials){
    this.qs.loginUser(credentials).subscribe(
      res=>{
        if(res.message==="Hi"){
          //save token to local storage
          localStorage.setItem("username",res.username)
          //update user login status
          this.qs.userLoginStatus=true;
          //after successfull login, navigate to userprofile
          this.rObj.navigateByUrl("/quiz")
        }
        else{
          alert(res.message)
        }
      },
      err=>{
        console.log("ERROR IS",err.message)
        alert("Something went wrong while login")
      }
    )
  }


}
