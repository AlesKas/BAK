 using System;
using System.Collections.Generic;
using System.Configuration;
using System.Data.SqlClient;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;

namespace CloudApp
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

        public bool getCreditals()
        {
            try
            {
                using (SqlConnection conn = new SqlConnection(ConfigurationManager.ConnectionStrings["dbConn"].ConnectionString))
                {
                    conn.Open();
                    SqlCommand command = new SqlCommand($"SELECT * FROM cloud WHERE username={this.username}", conn);

                    using (SqlDataReader dr = command.ExecuteReader())
                    {
                        while (dr.Read())
                        {
                            MessageBox.Show($"{dr[0]} {dr[1]} {dr[2]} {dr[3]}", "Info", MessageBoxButton.OK);
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
    }
}
