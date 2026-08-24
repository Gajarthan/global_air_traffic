# Global Air Traffic Tracker

![LastUpdated](https://img.shields.io/badge/last_updated-2026--08--24_11:31:17_UTC-green)

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

**Latest saved flight:** 2026-08-24 11:31:17 UTC
**Archive range:** 2026-03-27 22:00:26 UTC to 2026-08-24 11:31:17 UTC

- **231,520** saved flights
- **71,267** unique routes
- **144** countries touched by saved routes
- **100** airports in the archive
- **50** airlines identified
- **231,520** saved routes in the archive
- **1h 14m** average flight duration

### Carbon Footprint Estimate

- **2,792,040.9 tonnes** estimated CO2 emissions
- **161,857,442 km** total distance flown
- **857 km** average flight distance
*Based on ICAO avg: 115g CO2/passenger-km, ~150 passengers*

## Top Airlines

| # | Airline | Aircraft |
|---:|---------|--------:|
| 1 | Ryanair | 9297 |
| 2 | SkyWest Airlines | 8205 |
| 3 | EJA | 4472 |
| 4 | IndiGo | 3922 |
| 5 | American Airlines | 3786 |
| 6 | Southwest Airlines | 3574 |
| 7 | Delta Air Lines | 2958 |
| 8 | ENY | 2818 |
| 9 | LATAM Airlines | 2225 |
| 10 | AZU | 2148 |
| 11 | Vueling | 1975 |
| 12 | Lufthansa | 1883 |
| 13 | WIF | 1831 |
| 14 | LXJ | 1824 |
| 15 | easyJet | 1619 |
| 16 | Swiss International | 1551 |
| 17 | AXM | 1548 |
| 18 | EJU | 1477 |
| 19 | QLK | 1474 |
| 20 | United Airlines | 1471 |
| 21 | Alaska Airlines | 1397 |
| 22 | All Nippon Airways | 1385 |
| 23 | GLO | 1291 |
| 24 | WMT | 1279 |
| 25 | VIV | 1272 |
| 26 | PGT | 1265 |
| 27 | Air France | 1258 |
| 28 | Wizz Air | 1218 |
| 29 | AEE | 1154 |
| 30 | JetBlue | 1152 |

## Top Countries (by route endpoints)

| # | Country | Flights |
|---:|---------|--------:|
| 1 | 🇺🇸 US | 192846 |
| 2 | 🇪🇸 ES | 14853 |
| 3 | 🇧🇷 BR | 13520 |
| 4 | 🇦🇺 AU | 13156 |
| 5 | 🇨🇦 CA | 12765 |
| 6 | 🇮🇹 IT | 12571 |
| 7 | 🇮🇳 IN | 12209 |
| 8 | 🇩🇪 DE | 11382 |
| 9 | 🇬🇧 GB | 10907 |
| 10 | 🇨🇴 CO | 9614 |
| 11 | 🇯🇵 JP | 9437 |
| 12 | 🇫🇷 FR | 9255 |
| 13 | 🇹🇷 TR | 6840 |
| 14 | 🇬🇷 GR | 6821 |
| 15 | 🇲🇽 MX | 6432 |
| 16 | 🇨🇭 CH | 6155 |
| 17 | 🇳🇴 NO | 5707 |
| 18 | 🇲🇾 MY | 4130 |
| 19 | 🇹🇭 TH | 4084 |
| 20 | 🇿🇦 ZA | 4035 |
| 21 | 🇵🇱 PL | 3843 |
| 22 | 🇳🇿 NZ | 3212 |
| 23 | 🇵🇭 PH | 3182 |
| 24 | 🇬🇹 GT | 2903 |
| 25 | 🇰🇷 KR | 2723 |
| 26 | 🇭🇷 HR | 2657 |
| 27 | 🇲🇦 MA | 2348 |
| 28 | 🇲🇪 ME | 2129 |
| 29 | 🇳🇱 NL | 2069 |
| 30 | 🇮🇩 ID | 2010 |

## Busiest Airports (departures + arrivals across archive)

| # | Airport | City | Country | Flights |
|---:|---------|------|---------|--------:|
| 1 | Dallas-Fort Worth International Airport |  | US | 4820 |
| 2 | Denver International Airport |  | US | 3764 |
| 3 | Indira Gandhi International Airport |  | IN | 2823 |
| 4 | Tokyo International Airport |  | JP | 2817 |
| 5 | Guaymaral Airport |  | CO | 2654 |
| 6 | Harry Reid International Airport |  | US | 2492 |
| 7 | Zurich Airport |  | CH | 2419 |
| 8 | Minneapolis-St Paul International/Wold-Chamberlain Airport |  | US | 2363 |
| 9 | Eleftherios Venizelos International Airport |  | GR | 2330 |
| 10 | La Aurora Airport |  | GT | 2212 |
| 11 | El Dorado International Airport |  | CO | 2148 |
| 12 | Chicago O'Hare International Airport |  | US | 2096 |
| 13 | Salt Lake City International Airport |  | US | 2039 |
| 14 | Congonhas Airport |  | BR | 1972 |
| 15 | Phoenix Sky Harbor International Airport |  | US | 1958 |
| 16 | Frankfurt am Main International Airport |  | DE | 1848 |
| 17 | Capua Airport |  | IT | 1818 |
| 18 | Madrid Barajas International Airport |  | ES | 1816 |
| 19 | Guarulhos - Governador Andre Franco Montoro International Airport |  | BR | 1738 |
| 20 | Hartsfield/Jackson Atlanta International Airport |  | US | 1719 |
| 21 | Malpensa International Airport |  | IT | 1659 |
| 22 | General Edward Lawrence Logan International Airport |  | US | 1656 |
| 23 | Sydney Kingsford Smith International Airport |  | AU | 1636 |
| 24 | Charles de Gaulle International Airport |  | FR | 1607 |
| 25 | Macau International Airport |  | MO | 1603 |
| 26 | Ninoy Aquino International Airport |  | PH | 1532 |
| 27 | Charlotte/Douglas International Airport |  | US | 1507 |
| 28 | Kuala Lumpur International Airport |  | MY | 1493 |
| 29 | Barcelona International Airport |  | ES | 1455 |
| 30 | Atizapan De Zaragoza Airport |  | MX | 1400 |
| 31 | Enrique Olaya Herrera Airport |  | CO | 1388 |
| 32 | Viracopos International Airport |  | BR | 1374 |
| 33 | Bengaluru International Airport |  | IN | 1368 |
| 34 | Seattle-Tacoma International Airport |  | US | 1364 |
| 35 | Norman Y Mineta San Jose International Airport |  | US | 1360 |
| 36 | Don Mueang International Airport |  | TH | 1335 |
| 37 | Calgary International Airport |  | CA | 1317 |
| 38 | Oslo Gardermoen Airport |  | NO | 1294 |
| 39 | Vancouver International Airport |  | CA | 1256 |
| 40 | Vitoria/Foronda Airport |  | ES | 1256 |

## Top Routes (all saved history)

| # | From | To | Flights | Avg Duration | Distance | CO2 |
|---:|------|-----|--------:|------------:|--------:|----:|
| 1 | Guaymaral Airport (SKGY) | Guaymaral Airport (SKGY) | 1076 | 24m | - | - |
| 2 | Daniel K Inouye International Airport (PHNL) | Upolu Airport (PHUP) | 845 | 21m | 244 km | 3,558.1 t |
| 3 | Tokyo International Airport (RJTT) | Hofu Airport (RJOF) | 585 | 1h 6m | 770 km | 7,771.3 t |
| 4 | Ninoy Aquino International Airport (RPLL) | Wasig Airport (RPVL) | 581 | 24m | 225 km | 2,254.0 t |
| 5 | Enrique Olaya Herrera Airport (SKMD) | Enrique Olaya Herrera Airport (SKMD) | 563 | 8m | - | - |
| 6 | La Aurora Airport (MGGT) | La Aurora Airport (MGGT) | 517 | 12m | - | - |
| 7 | Madrid Barajas International Airport (LEMD) | Vitoria/Foronda Airport (LEVT) | 382 | 27m | 275 km | 1,810.1 t |
| 8 | VGZR (VGZR) | Shah Amanat International Airport (VGEG) | 357 | 35m | - | - |
| 9 | Indira Gandhi International Airport (VIDP) | Yongphulla Airport (VQ10) | 357 | 1h 50m | 1,423 km | 8,761.3 t |
| 10 | Oslo Gardermoen Airport (ENGM) | Sogndal Airport (ENSG) | 335 | 44m | 241 km | 1,391.5 t |
| 11 | O. R. Tambo International Airport (FAOR) | Newcastle Airport (FANC) | 327 | 21m | 250 km | 1,412.4 t |
| 12 | Don Mueang International Airport (VTBD) | Surat Thani Airport (VTSB) | 324 | 44m | 555 km | 3,102.5 t |
| 13 | Tokyo International Airport (RJTT) | Iwakuni Marine Corps Air Station (RJOI) | 316 | 1h 7m | 706 km | 3,847.3 t |
| 14 | El Dorado International Airport (SKBO) | Perales Airport (SKIB) | 312 | 14m | 114 km | 611.9 t |
| 15 | Provo Municipal Airport (KPVU) | Nephi Municipal Airport (KU14) | 307 | 22m | 55 km | 291.8 t |
| 16 | Eleftherios Venizelos International Airport (LGAV) | Santorini Airport (LGSR) | 305 | 24m | 218 km | 1,149.1 t |
| 17 | Indira Gandhi International Airport (VIDP) | Pune Airport (VAPO) | 300 | 1h 38m | 1,156 km | 5,984.9 t |
| 18 | Tokyo International Airport (RJTT) | Saga Airport (RJFS) | 299 | 1h 25m | 910 km | 4,692.0 t |
| 19 | La Aurora Airport (MGGT) | Coban Airport (MGCB) | 285 | 19m | 99 km | 488.2 t |
| 20 | Bergen Airport Flesland (ENBR) | Ørsta-Volda Airport Hovden (ENOV) | 281 | 27m | 215 km | 1,040.7 t |
| 21 | Kawaihapai Airfield (PHDH) | Kawaihapai Airfield (PHDH) | 275 | 12m | - | - |
| 22 | Congonhas Airport (SBSP) | Destilaria Medasa Airport (SJNQ) | 270 | 1h 14m | 961 km | 4,475.4 t |
| 23 | Bodø Airport (ENBO) | ENEN (ENEN) | 267 | 13m | - | - |
| 24 | Gimpo International Airport (RKSS) | G 802 Airport (RKD1) | 266 | 29m | 304 km | 1,394.4 t |
| 25 | Reykjavik Airport (BIRK) | Hveravellir Airport (BIHI) | 263 | 19m | 144 km | 654.2 t |
| 26 | Ninoy Aquino International Airport (RPLL) | Moises R. Espinosa Airport (RPVJ) | 260 | 31m | 369 km | 1,655.0 t |
| 27 | Kuala Lumpur International Airport (WMKK) | Batu Pahat Airport (WMAB) | 253 | 19m | 165 km | 719.7 t |
| 28 | Kuala Lumpur International Airport (WMKK) | Jendarata Airport (WMAJ) | 249 | 15m | 154 km | 659.8 t |
| 29 | Cancun International Airport (MMUN) | Atizapan De Zaragoza Airport (MMJC) | 247 | 1h 50m | 1,304 km | 5,556.9 t |
| 30 | La Aurora Airport (MGGT) | Copan Ruinas Airport (MHRU) | 245 | 28m | 152 km | 640.3 t |

## Recent Flights

| Callsign | Airline | From | To | Departure | Arrival | Duration |
|----------|---------|------|-----|-----------|---------|----------|
| DHXCF | DHX | Gelnhausen Airport (EDFG) | Wurzburg-Schenkenturm Airport (EDFW) | 2026-08-24 11:13 UTC | 2026-08-24 11:31 UTC | 17m |
| DEBFT | DEB | Gunzburg-Donauried Airport (EDMG) | Mengen-Hohentengen Airport (EDTM) | 2026-08-24 10:02 UTC | 2026-08-24 11:24 UTC | 1h 21m |
| GENBW | GEN | Lasham Airport (EGHL) | Lasham Airport (EGHL) | 2026-08-24 11:12 UTC | 2026-08-24 11:24 UTC | 12m |
| PSDOR | PSD | Congonhas Airport (SBSP) | Clube do Ceu Airport (SDIN) | 2026-08-24 10:45 UTC | 2026-08-24 11:16 UTC | 30m |
| GBBMB | GBB | North Weald Airport (EGSX) | North Weald Airport (EGSX) | 2026-08-24 10:36 UTC | 2026-08-24 11:07 UTC | 31m |
| N24PL |  | Flying Cloud Airport (KFCM) | Cox-Coyour Memorial Field (59MN) | 2026-08-24 10:26 UTC | 2026-08-24 11:07 UTC | 40m |
| AMQ4F | AMQ | Copernicus Wrocław Airport (EPWR) | Otocac Airport (LDRO) | 2026-08-24 09:58 UTC | 2026-08-24 11:01 UTC | 1h 2m |
| FLE636 | FLE | Edmonton International Airport (CYEG) | Toronto Pearson International Airport (CYYZ) | 2026-08-24 07:38 UTC | 2026-08-24 10:58 UTC | 3h 20m |
| JANET11 | JAN | Harry Reid International Airport (KLAS) | KXTA (KXTA) | 2026-08-24 10:42 UTC | 2026-08-24 10:54 UTC | 12m |
| ACA364 | Air Canada | Vancouver International Airport (CYVR) | Stanley Airport (CCW4) | 2026-08-24 05:41 UTC | 2026-08-24 10:54 UTC | 5h 13m |
| AIQ3256 | AIQ | Don Mueang International Airport (VTBD) | Khon Kaen Airport (VTUK) | 2026-08-24 10:13 UTC | 2026-08-24 10:51 UTC | 38m |
| N555WL |  | Oakland County International Airport (KPTK) | Roscommon Conservation Airport (K3RC) | 2026-08-24 10:24 UTC | 2026-08-24 10:50 UTC | 26m |
| N666ES |  | Wings Field (KLOM) | Morristown Municipal Airport (KMMU) | 2026-08-24 10:27 UTC | 2026-08-24 10:49 UTC | 21m |
| WZZ84 | Wizz Air | Budapest Ferenc Liszt International Airport (LHBP) | Berlin Brandenburg Airport (EDDB) | 2026-08-24 09:38 UTC | 2026-08-24 10:49 UTC | 1h 11m |
| IGO7642 | IndiGo | Safdarjung Airport (VIDD) | Jaipur International Airport (VIJP) | 2026-08-24 10:19 UTC | 2026-08-24 10:43 UTC | 23m |
| SXGAP | SXG | Megara Airport (LGMG) | Milos Airport (LGML) | 2026-08-24 09:05 UTC | 2026-08-24 10:42 UTC | 1h 37m |
| N522TG |  | Oakland County International Airport (KPTK) | Lakes Of The North Airport (K4Y4) | 2026-08-24 09:58 UTC | 2026-08-24 10:42 UTC | 44m |
| ZSORP | ZSO | O. R. Tambo International Airport (FAOR) | Thabazimbi Airport (FATI) | 2026-08-24 10:03 UTC | 2026-08-24 10:35 UTC | 31m |
| AUA707X | Austrian Airlines | Vienna International Airport (LOWW) | Sibiu International Airport (LRSB) | 2026-08-24 09:45 UTC | 2026-08-24 10:31 UTC | 46m |
| INICC | INI | Biella / Cerrione Airport (LILE) | Torino / Caselle International Airport (LIMF) | 2026-08-24 10:09 UTC | 2026-08-24 10:31 UTC | 21m |

---

![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenSky](https://img.shields.io/badge/data-OpenSky_Network-00aaff)](https://opensky-network.org/)
