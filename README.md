# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--22_10:16:34_UTC-green)

![Flight Map](images/flight_map.png)

## About

Historical archive of saved air traffic routes collected from the [OpenSky Network](https://opensky-network.org/) API. This repository keeps appending completed flights to `data/flights/` and rebuilds the visuals from the full archive.

**Data Source:** Saved route files in `data/flights/` (originally fetched from OpenSky `/flights/all`)

**Update Frequency:** Every 5 minutes via GitHub Actions

**How it works:**
- Fetches recently completed routes from OpenSky
- Saves each route as a JSON file in `data/flights/`
- Rebuilds aggregate statistics from all saved historical routes
- Generates a historical route map and archive summary
- Generates daily reports, weekly leaderboards, and timelapse GIFs

## Route Timelapse

![Timelapse](images/timelapse.gif)

## Archive Snapshot

**Latest saved flight:** 2026-08-22 10:16:34 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-22 10:16:34 UTC

- **225,142** saved flights
- **70,112** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **225,142** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,712,297.6 tonnes** estimated CO2 emissions
- **157,234,642 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9027 |
| 2 | SkyWest Airlines | 7997 |
| 3 | EJA | 4353 |
| 4 | IndiGo | 3806 |
| 5 | American Airlines | 3705 |
| 6 | Southwest Airlines | 3524 |
| 7 | Delta Air Lines | 2879 |
| 8 | ENY | 2759 |
| 9 | LATAM Airlines | 2140 |
| 10 | AZU | 2074 |
| 11 | Vueling | 1899 |
| 12 | Lufthansa | 1851 |
| 13 | WIF | 1789 |
| 14 | LXJ | 1777 |
| 15 | easyJet | 1557 |
| 16 | Swiss International | 1497 |
| 17 | AXM | 1487 |
| 18 | QLK | 1421 |
| 19 | EJU | 1418 |
| 20 | United Airlines | 1417 |
| 21 | Alaska Airlines | 1369 |
| 22 | All Nippon Airways | 1353 |
| 23 | GLO | 1244 |
| 24 | PGT | 1237 |
| 25 | VIV | 1231 |
| 26 | Air France | 1223 |
| 27 | WMT | 1204 |
| 28 | Wizz Air | 1160 |
| 29 | JetBlue | 1129 |
| 30 | AEE | 1121 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 188738 |
| 2 | 🇪🇸 ES | 14416 |
| 3 | 🇧🇷 BR | 13053 |
| 4 | 🇦🇺 AU | 12772 |
| 5 | 🇨🇦 CA | 12480 |
| 6 | 🇮🇹 IT | 12050 |
| 7 | 🇮🇳 IN | 11866 |
| 8 | 🇩🇪 DE | 11083 |
| 9 | 🇬🇧 GB | 10555 |
| 10 | 🇨🇴 CO | 9256 |
| 11 | 🇯🇵 JP | 9174 |
| 12 | 🇫🇷 FR | 8987 |
| 13 | 🇹🇷 TR | 6579 |
| 14 | 🇬🇷 GR | 6567 |
| 15 | 🇲🇽 MX | 6259 |
| 16 | 🇨🇭 CH | 5928 |
| 17 | 🇳🇴 NO | 5568 |
| 18 | 🇲🇾 MY | 3960 |
| 19 | 🇿🇦 ZA | 3891 |
| 20 | 🇹🇭 TH | 3852 |
| 21 | 🇵🇱 PL | 3729 |
| 22 | 🇳🇿 NZ | 3138 |
| 23 | 🇵🇭 PH | 3074 |
| 24 | 🇬🇹 GT | 2850 |
| 25 | 🇰🇷 KR | 2674 |
| 26 | 🇭🇷 HR | 2526 |
| 27 | 🇲🇦 MA | 2262 |
| 28 | 🇲🇪 ME | 2007 |
| 29 | 🇳🇱 NL | 2003 |
| 30 | 🇮🇩 ID | 1943 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4706 |
| 2 | Denver International Airport |  | US | 3670 |
| 3 | Tokyo International Airport |  | JP | 2741 |
| 4 | Indira Gandhi International Airport |  | IN | 2734 |
| 5 | Guaymaral Airport |  | CO | 2630 |
| 6 | Harry Reid International Airport |  | US | 2465 |
| 7 | Zurich Airport |  | CH | 2334 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2301 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2275 |
| 10 | La Aurora Airport |  | GT | 2172 |
| 11 | El Dorado International Airport |  | CO | 2080 |
| 12 | Chicago O'Hare International Airport |  | US | 2048 |
| 13 | Salt Lake City International Airport |  | US | 1979 |
| 14 | Phoenix Sky Harbor International Airport |  | US | 1926 |
| 15 | Congonhas Airport |  | BR | 1909 |
| 16 | Frankfurt am Main International Airport |  | DE | 1816 |
| 17 | Madrid Barajas International Airport |  | ES | 1759 |
| 18 | Capua Airport |  | IT | 1731 |
| 19 | Hartsfield/Jackson Atlanta International Airport |  | US | 1678 |
| 20 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1667 |
| 21 | General Edward Lawrence Logan International Airport |  | US | 1634 |
| 22 | Macau International Airport |  | MO | 1592 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1589 |
| 24 | Malpensa International Airport |  | IT | 1579 |
| 25 | Charles de Gaulle International Airport |  | FR | 1558 |
| 26 | Charlotte/Douglas International Airport |  | US | 1483 |
| 27 | Ninoy Aquino International Airport |  | PH | 1469 |
| 28 | Kuala Lumpur International Airport |  | MY | 1440 |
| 29 | Barcelona International Airport |  | ES | 1390 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1368 |
| 31 | Bengaluru International Airport |  | IN | 1341 |
| 32 | Norman Y Mineta San Jose International Airport |  | US | 1333 |
| 33 | Seattle-Tacoma International Airport |  | US | 1329 |
| 34 | Viracopos International Airport |  | BR | 1323 |
| 35 | Enrique Olaya Herrera Airport |  | CO | 1303 |
| 36 | Calgary International Airport |  | CA | 1279 |
| 37 | Don Mueang International Airport |  | TH | 1265 |
| 38 | Oslo Gardermoen Airport |  | NO | 1254 |
| 39 | Vitoria/Foronda Airport |  | ES | 1242 |
| 40 | Amsterdam Airport Schiphol |  | NL | 1216 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1072 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 815 | 21m | 244 km | 3,431.7 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 561 | 1h 7m | 770 km | 7,452.5 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 555 | 24m | 225 km | 2,153.1 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 527 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 510 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 378 | 27m | 275 km | 1,791.2 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 354 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 338 | 1h 50m | 1,423 km | 8,295.1 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 327 | 44m | 241 km | 1,358.3 t |
| 11 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 312 | 1h 7m | 706 km | 3,798.6 t |
| 12 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 13 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 301 | 21m | 250 km | 1,300.1 t |
| 14 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 298 | 22m | 55 km | 283.2 t |
| 16 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 286 | 1h 38m | 1,156 km | 5,705.6 t |
| 17 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 286 | 44m | 555 km | 2,738.6 t |
| 18 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 283 | 24m | 218 km | 1,066.2 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 280 | 19m | 99 km | 479.6 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 275 | 27m | 215 km | 1,018.5 t |
| 21 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 265 | 29m | 304 km | 1,389.2 t |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 264 | 1h 14m | 961 km | 4,375.9 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 262 | 13m | - | - |
| 24 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 259 | 31m | 369 km | 1,648.6 t |
| 25 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 258 | 12m | - | - |
| 26 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 257 | 19m | 144 km | 639.3 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 244 | 1h 50m | 1,304 km | 5,489.4 t |
| 29 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 238 | 28m | 152 km | 622.0 t |
| 30 | Harry Reid International Airport (KLAS) | Reno/Tahoe International Airport (KRNO) | 235 | 50m | 556 km | 2,252.7 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| RYR69CX | Ryanair | Vienna International Airport (LOWW) | Kalamata Airport (LGKL) | 2026-08-22 08:36 UTC | 2026-08-22 10:16 UTC | 1h 40m |
| LZKPR | LZK | Ihtiman Airport (LBHT) | Ihtiman Airport (LBHT) | 2026-08-22 09:35 UTC | 2026-08-22 10:04 UTC | 29m |
| WWF287 | WWF | Roberts Field/Redmond Municipal Airport (KRDM) | Josephine Ranch Airport (2ID3) | 2026-08-22 07:47 UTC | 2026-08-22 09:56 UTC | 2h 8m |
| A7GAC |  | Doha International Airport (OTBD) | Persian Gulf International Airport (OIBP) | 2026-08-22 09:12 UTC | 2026-08-22 09:56 UTC | 43m |
| FGBLH | FGB | Saint-Jean-en-Royans Airport (LFKE) | L'alpe D'huez Airport (LFHU) | 2026-08-22 08:41 UTC | 2026-08-22 09:35 UTC | 53m |
| GGWMB | GGW | Turweston Airport (EGBT) | Turweston Airport (EGBT) | 2026-08-22 08:04 UTC | 2026-08-22 09:35 UTC | 1h 30m |
| WZZ84 | Wizz Air | Budapest Ferenc Liszt International Airport (LHBP) | Berlin Brandenburg Airport (EDDB) | 2026-08-22 08:21 UTC | 2026-08-22 09:33 UTC | 1h 11m |
| GCDOK | GCD | Old Sarum Airfield (EGLS) | Isle of Wight / Sandown Airport (EGHN) | 2026-08-22 08:51 UTC | 2026-08-22 09:31 UTC | 40m |
| IGO7425 | IndiGo | Indira Gandhi International Airport (VIDP) | Bareilly Air Force Station (VIBY) | 2026-08-22 08:51 UTC | 2026-08-22 09:29 UTC | 37m |
| RYR91SK | Ryanair | Leeds Bradford Airport (EGNM) | Ussel-Thalamy Airport (LFCU) | 2026-08-22 08:11 UTC | 2026-08-22 09:25 UTC | 1h 13m |
| ICE16Y | ICE | Reykjavik Airport (BIRK) | Melanes Airport (BIMN) | 2026-08-22 09:01 UTC | 2026-08-22 09:25 UTC | 23m |
| LLR860 | LLR | Hissar Airport (VIHR) | Jaipur International Airport (VIJP) | 2026-08-22 08:55 UTC | 2026-08-22 09:21 UTC | 26m |
| LIFELN3 | LIF | Northern Colorado Regional Airport (KFNL) | Northern Colorado Regional Airport (KFNL) | 2026-08-22 09:19 UTC | 2026-08-22 09:20 UTC | 1m |
| RYR2MP | Ryanair | Madrid Barajas International Airport (LEMD) | Bergamo / Orio Al Serio Airport (LIME) | 2026-08-22 07:42 UTC | 2026-08-22 09:19 UTC | 1h 37m |
| IGO502F | IndiGo | Indira Gandhi International Airport (VIDP) | Ambala Air Force Station (VIAM) | 2026-08-22 08:57 UTC | 2026-08-22 09:18 UTC | 21m |
| SIO619 | SIO | Rimini / Miramare - Federico Fellini International Airport (LIPR) | Samedan Airport (LSZS) | 2026-08-22 08:35 UTC | 2026-08-22 09:17 UTC | 42m |
| OKCUN20 | OKC | Brno-Turany Airport (LKTB) | Brno-Turany Airport (LKTB) | 2026-08-22 08:13 UTC | 2026-08-22 09:14 UTC | 1h 1m |
| SXS6DP | SXS | Vienna International Airport (LOWW) | Antalya International Airport (LTAI) | 2026-08-22 06:38 UTC | 2026-08-22 09:12 UTC | 2h 33m |
| EJU38JM | EJU | Nice-Cote d'Azur Airport (LFMN) | Capua Airport (LIAU) | 2026-08-22 08:18 UTC | 2026-08-22 09:11 UTC | 52m |
| VOE84KY | VOE | Menorca Airport (LEMH) | Santander Airport (LEXJ) | 2026-08-22 08:02 UTC | 2026-08-22 09:10 UTC | 1h 8m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
