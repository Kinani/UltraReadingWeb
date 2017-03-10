using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using System.Net;
using System.Threading.Tasks;
using UltraReadingWeb.Models;
using UltraReadingWeb.Common;

namespace UltraReadingWeb.Controllers
{
    public class UltraReadingController : Controller
    {
        [ActionName("Index")]
        public async Task<ActionResult> IndexAsync()
        {
            var items = await DocDBRepo<UltraReading>.GetItemsAsync(r => r.Reading != string.Empty);
            return View(items.Reverse().Take(15));
        }
    }
}