/*
 * WORK TIME CONTROL
 * 
 *
 * This Script is to verify the hours I can leave the office
 */

using System;

// Variables
var interval = new TimeSpan(1,0,0); // 1h interval
var hourDay = new TimeSpan(8,48,0); // 8h48 of worktime daily
var maxTimeDay = new TimeSpan(10,0,0); // 10h of maximum time daily

Console.Write("> Enter the starting work time (HH:MM) : ");
#pragma warning disable CS8600
string entry = Console.ReadLine();
Console.WriteLine("\n");

#pragma warning disable CS8602
if (entry.Contains(":"))
{
  string[] entrySplit = entry.Split(":");
  var startingTime = new TimeSpan(Int32.Parse(entrySplit[0]), Int32.Parse(entrySplit[1]), 0);
  var expectedLeave = startingTime + interval + hourDay;
  var maximumLeave = startingTime + interval + maxTimeDay;

  // Show the start time in console
  Console.Write("STARTING TIME: ");
  Console.ForegroundColor = ConsoleColor.Magenta;
  Console.WriteLine($"{startingTime}");
  Console.ResetColor();

  // Show the expected end time in console
  Console.Write("EXPECTED TIME LEAVE: ");
  Console.ForegroundColor = ConsoleColor.Green;
  Console.WriteLine($"{expectedLeave}");
  Console.ResetColor();

  // Show the maximum end time in console
  Console.Write("MAXIMUM TIME LEAVE: ");
  Console.ForegroundColor = ConsoleColor.Red;
  Console.WriteLine($"{maximumLeave}");
  Console.ResetColor();

}
else
{
  Console.WriteLine("ERROR! Time structure not valid.");
}

Console.WriteLine("\n");
