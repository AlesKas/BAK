using System;
using CloudApp.models;
using System.Collections.Generic;
using System.Configuration;
using System.Data.SqlClient;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;

namespace CloudApp.handlers
{
    class SQLhandler
    {
        private string username { get; }
        private string password { get; }
        private string DBusername { get; set; }
        private string DBpassword { get; set; }

        public SQLhandler()
        {

        }

        public SQLhandler(string username, string password)
        {
            this.username = username;
            this.password = password;
        }

        private string getConnectionString()
        {
            return ConfigurationManager.ConnectionStrings["dbConn"].ConnectionString;
        }

        public bool getCreditals()
        {
            try
            {
                string commandString = "SELECT * FROM cloud WHERE username=@username;";
                using (SqlConnection conn = new SqlConnection(getConnectionString()))
                {
                    conn.Open();
                    using (SqlCommand command = new SqlCommand())
                    {
                        command.Connection = conn;
                        command.CommandText = commandString;
                        command.Parameters.AddWithValue("@username", this.username);
                        command.ExecuteNonQuery();

                        using (SqlDataReader dr = command.ExecuteReader())
                        {
                            while (dr.Read())
                            {
                                MessageBox.Show($"{dr[0]} {dr[1]} {dr[2]} {dr[3]}", "Info", MessageBoxButton.OK);
                            }
                        }
                    }
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Error", MessageBoxButton.OK);
                return false;
            }
            return true;
        }

        public bool isUsernameAvailable(string usernameToValidate)
        {
            string commandString = $"SELECT COUNT(*) FROM cloudUsers WHERE username={usernameToValidate};";
            try
            {
                using (SqlConnection conn = new SqlConnection(getConnectionString()))
                {
                    using (SqlCommand command = new SqlCommand())
                    {
                        command.Connection = conn;
                        command.CommandText = commandString;
                        conn.Open();
                        
                        int count = Convert.ToInt32(command.ExecuteScalar());
                        if (count > 0)
                            return false;
                    }
                }
            }
            catch (Exception e)
            {
                return true;
            }
            return false;
        }

        public bool createUser(User newUser)
        {
            try
            {
                string commandString = "INSERT INTO cloudUsers (username, password, admin, firstName, lastName, email) VALUES(@username, @password, @admin, @firstName, @lastname, @email);";
                using (SqlConnection conn = new SqlConnection(getConnectionString()))
                {
                    using(SqlCommand command = new SqlCommand())
                    {
                        command.Connection = conn;
                        command.CommandText = commandString;
                        command.Parameters.AddWithValue("@username", newUser.username);
                        command.Parameters.AddWithValue("@password", newUser.password);
                        command.Parameters.AddWithValue("@admin", newUser.admin);
                        command.Parameters.AddWithValue("@firstName", newUser.firstName);
                        command.Parameters.AddWithValue("@lastname", newUser.lastName);
                        command.Parameters.AddWithValue("@email", newUser.email);
                        conn.Open();
                        command.ExecuteNonQuery();
                        return true;
                    }
                }
            }
            catch (Exception e)
            {
                MessageBox.Show(e.Message, "Error", MessageBoxButton.OK);
            }
            return false;
        }
    }
}
