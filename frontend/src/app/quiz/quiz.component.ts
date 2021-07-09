import { Component, OnInit } from '@angular/core';
import { QuizsService } from '../quizs.service';

@Component({
  selector: 'app-quiz',
  templateUrl: './quiz.component.html',
  styleUrls: ['./quiz.component.css']
})
export class QuizComponent implements OnInit {
  data:any
  cnt:number=0
  c:number=0
  constructor(private qs:QuizsService) { }

  ngOnInit(): void {
    this.qs.getData().subscribe(
      dObj=>{
        this.data=dObj
      },
      err=>{}
    )
  }

  onSubmit(value){
    console.log(value)
    for (let i of this.data) {
      if(i.cans==value[this.c]){
        this.cnt+=1
      }
      this.c+=1
    }
    console.log(this.cnt)
    //console.log(this.c)
  }



}
