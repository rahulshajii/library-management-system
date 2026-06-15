import { Component, OnInit } from '@angular/core';
import { DashboardService } from '../../services/dashboard.service';

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.css'
})
export class DashboardComponent implements OnInit {

  dashboardData: any = {};

  constructor(private dashboardService: DashboardService) {}
ngOnInit(): void {
  this.dashboardService.getDashboard().subscribe({
    next: (data) => {
      console.log(data);   // Optional: keep for debugging
      this.dashboardData = data;
    },
    error: (err) => {
      console.error(err);  // Log the error in the console
    }
  });
}


}
