import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';

import { MemberService } from '../../services/member.service';

@Component({
  selector: 'app-members',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './members.component.html',
  styleUrl: './members.component.css'
})
export class MembersComponent implements OnInit {

  members: any[] = [];

  constructor(private memberService: MemberService) {}

  ngOnInit(): void {

    this.memberService.getMembers().subscribe({

      next: (data) => {

        this.members = data;

      },

      error: (err) => {

        console.log(err);

      }

    });

  }

}
