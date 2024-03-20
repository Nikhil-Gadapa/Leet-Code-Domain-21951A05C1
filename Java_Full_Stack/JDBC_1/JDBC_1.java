import java.sql.*;
import java.util.*;

class JDBC_1{
	public static void main(String rags[]) throws Exception{
		//the following driver class connects us oracle DB
		
		Class.forName("oracle.jdbc.driver.OracleDriver");
		
		Connection con=DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:XE",
		"pat","pat");
		
		Statement stmt=con.createStatement();
		
		Scanner sc=new Scanner(System.in);
		
		System.out.println("Enter First Name");
		String fname=sc.next();
		System.out.println("Enter Last Name:");
		String lname=sc.next();
		System.out.println("Enter Email:");
		String email=sc.next();
		System.out.println("Enter Pass:");
		String pass=sc.next();
		System.out.println("Enter Mobile:");
		long mobile=sc.nextLong();
		sc.nextLine();
		System.out.println("Enter Address:");
		String address=sc.next();
		
		int regid=0;
		ResultSet rs=stmt.executeQuery("Select max(regid) from register");
		if(rs.next()){
			regid=rs.getInt(1);
		}
		regid++;
		String sql= "insert into register values('"+regid+"','"+fname+"','"+lname+"','"+email+"','"+pass+"','"+mobile+"','"+address+"')";
		
		int i=stmt.executeUpdate(sql);
		
		if(i==1)
			System.out.println(i+"record inserted");
		
		rs.close(); stmt.close(); con.close();
	}
}
