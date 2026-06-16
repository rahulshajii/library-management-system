
import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { DashboardService } from '../../services/dashboard.service';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.css'
})
export class DashboardComponent implements OnInit {

  dashboardData: any = {};
  recentTransactions: any[] = [];

  constructor(private dashboardService: DashboardService) {}

  ngOnInit(): void {

    console.log("Dashboard loaded");

    this.dashboardService.getDashboard().subscribe({

      next: (data) => {

        console.log("SUCCESS", data);

        this.dashboardData = data;
        this.recentTransactions = data.recent_transactions;

      },

      error: (err) => {

        console.log("ERROR", err);

      }

    });

  }

}
