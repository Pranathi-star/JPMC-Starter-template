import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { QuizsService } from '../quizs.service';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent implements OnInit {

  constructor(private qs:QuizsService,private rObj:Router) { }

  ngOnInit(): void {
  }
  
  onSignUp(userObj){
    this.qs.createUser(userObj).subscribe(
      res=>{
        if(res.message==="done"){
          alert("User created")
          this.rObj.navigateByUrl("/login")
        }
        else{
          alert(res.message)
        }
      },
      err=>{
        console.log("ERROR IS",err.message)
        alert("Something went wrong in user creation")
      }
    )
  }

}
