 using System;
using System.Collections.Generic;
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

        public bool getCreditals()
        {
            try
            {
                using (SqlConnection conn = new SqlConnection(@"Data Source=localhost;Initial Catalog=CloudUsers;Integrated Security=True"))
                {
                    conn.Open();
                    SqlCommand command = new SqlCommand("SELECT * FROM cloud WHERE ");

                    using (SqlDataReader dr = command.ExecuteReader())
                    {
                        while (dr.Read())
                        {

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
