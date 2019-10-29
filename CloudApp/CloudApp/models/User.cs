using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CloudApp.models
{
    class User
    {
        private int Id { get; }
        private string username { get; set; }
        private string password { get; set; }
        private bool admin { get; set; }
        private string firstName { get; set; }
        private string lastName { get; set; }
        private string email { get; set; }
    }
}
