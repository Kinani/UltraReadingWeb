using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using Newtonsoft.Json;

namespace UltraReadingWeb.Models
{
    public class UltraReading
    {
        [JsonProperty(PropertyName = "id")]
        public string Id { get; set; }
        [JsonProperty(PropertyName = "reading")]
        public string Reading { get; set; }
    }
}