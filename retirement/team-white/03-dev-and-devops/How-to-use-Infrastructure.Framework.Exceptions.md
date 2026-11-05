# How to use Infrastructure.Framework.Exceptions

> Source: [Team White SharePoint](https://ascensus0.sharepoint.com/sites/TeamWhiteCF/SitePages/MTP-How-to-use-Infrastructure.Framework.Exceptions-294990656.aspx) | Created: 2024-12-17 | Last modified: 2025-07-28 | Author: Eddie Hooper | Last editor: Eddie Hooper

---

Intended use of Infrastructure.Framework.Exceptions library ->

The main idea of this library is to log as specific application-level exception as possible and log it only once at a place where exception occurred with the values (if possible) that caused an exception to happen and then bubble up to the original caller through all the application layers as a PassThroughException to avoid logging it again.

This library is broken down into a set of Exception Handlers (one to many for each application layer) and Exception Types.
Library works with Handled and Unhandled exceptions. Handled exceptions are the once throwed from code and they contain 'Custom' within an Exception name for identification.

It is very important to note that in order to get the most out of this library the try catch block with the corresponding Handle Exception call must be implemented for each method (any scope) within each application layer.

Here is the sample usage of **Unhandled** Exceptions for the app layers library currently supports:
try
{
    ; //- app code
}
catch (Exception ex)
{
    AppExceptionHandler.HandleException(ex);
}

**try
{
    ; //- app code
}
catch (Exception ex)
{
    ManagerExceptionHandler.HandleException(ex);
}**

**try
{
    ; //- app code
}
catch (Exception ex)
{
    EngineExceptionHandler.HandleException(ex);
}**

**try
{
    ; //- app code
}
catch (Exception ex)
{
    ResourceAccessExternalExceptionHandler.HandleException(ex);
}**

try
{
    ; //- app code
}
catch (Exception ex)
{
    ResourceAccessFileExceptionHandler.HandleException(ex);
}

or

try
{
    ; //- app code
}
catch (Exception ex)
{
    ResourceAccessFileExceptionHandler.HandleException(ex, new Dictionary<string, object>
{
    { "SectionName", cellInfo.SectionName },
    { "LineNumber", cellInfo.RowNumber },
    { "FieldPostion", cellInfo.CellPos },
    { "FieldValue", value },
});

**}**

try
{
    ; //- app code
}
catch (Exception ex)
{
    ResourceAccessExceptionHandler.HandleException(ex);
}

or

try
{
    ; //- app code
}
catch (Exception ex)
{
    ResourceAccessExceptionHandler.HandleException(ex, new Dictionary<string, object>
  {
    { "SQL", query },
    { "@TrusteeAcctId", trusteeAcctId },
    { "@ActionType", (int)actionType },
    { "@FileName", fileName }
});
}

Example of using Constants class to build and throw **Handled** exceptions for any application level (idea is the same for any layer of the program just different exception type is used):

**try
{
    throw new EngineExceptionCustom(string.Format(Constants.ExceptionMessages.Engine.ACTION_NOT_FOUND, actionType.ToString()));
}
catch (Exception ex)
{
    EngineExceptionHandler.HandleException(ex);
}**

or

**try
{
    throw new EngineExceptionCustom(string.Format(Constants.ExceptionMessages.Engine.ACTION_NOT_FOUND, actionType.ToString()), new ArgumentOutOfRangeException(actionType.ToString()));
},
catch (Exception ex)
{
    EngineExceptionHandler.HandleException(ex);
}**
